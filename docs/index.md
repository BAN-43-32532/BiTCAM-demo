---
layout: default
---

## One-Step Generation

Flow matching framework allows us generate data by solving ODE.

$x_t=\alpha_tx_0+\beta_tx_1,~x_0\sim p_\text{data},~x_1\sim\mathcal{N}(0,I)$

$\frac{\mathrm{d}}{\mathrm{d}\!t}X(t)=v(X(t),t)$, $v(x,t)=\mathbb E[\alpha_t^\prime x_0+\beta_t^\prime x_1\vert x_t=x]$

However, solving the ODE is time-consuming. We want to use a neural network directly solve the velocity ODE to realize few-step generation.

We consider $f(x,t,s)$, which is the solution operator of velocity ODE; it solves the velocity ODE with initial condition $X(t)=x$ to time $s$.

---

To realize few-step generation, we need to use a model $f_\theta(x,t,s)$ to approximate the ground truth solution operator $f(x,t,s)$ given by flow matching velocity field.

We discovered a simple and efficient learning method with equation:

$f_{\theta1}^\prime (x,t,s)v(x,t)+f_{\theta2}^\prime (x,t,s)=0$ with $f_\theta(x,t,t)=x$

$f_\theta(x,t,t)=x$ gives $f_{\theta1}^\prime (x,t,t)=\mathbf{I}$ and $f_{\theta2}^\prime (x,t,t)=-f_{\theta3}^\prime (x,t,t)$

Thus, when $t=s$, it gives flow matching loss $f_{\theta3}^\prime (x,t,t)=v(x,t)$

For general situations, the Taylor's expansion gives us a consistency loss:

$0=f_{\theta1}^\prime (x,t,s)v(x,t)+f_{\theta2}^\prime (x,t,s)=\frac{1}{t-l}[f_\theta(x,t,s)-f_\theta(x+v(x,t)(l-t),l,s)]+\mathcal{O}(t-l)$

---

Velocity Loss: $\mathbb E_{x_t,t}\left[w_v(t,\mathrm{MSE_\mathrm{Loss}})\cdot\frac{1}{D}\left\lVert f_{\theta3}^\prime(x_t,t,t)-v(x_t,t)\right\rVert_2^2\right]$

Consistency Loss: $\mathbb E_{x_t,t,s}\left[w_c(t,s,\mathrm{MSE_\mathrm{Loss}})\cdot \frac{1}{D}\left\lVert\frac{f_\theta(x,t,s)-f_{\theta^-}(x+v(x,t)(l-t),l,s)}{t-l}\right\rVert_2^2\right]$

$\theta^-$ means stop gradient operation and $D$ is the data dimension.

Set $l=t+(s-t)\cdot0.1\cdot0.01^{\text{cur-step}/\text{tot-step}}$, which will get close to $t$ gradually.

$w_v(t,\mathrm{MSE_\mathrm{Loss}})$ and $w_c(t,s,\mathrm{MSE_\mathrm{Loss}})$ are dynamic scale functions.

---

Consider $f_\theta(x,t,s)=a(t,s)x+b(t,s)\mathrm{NN}_\theta(x,t,s)$.

We can parameterize the model through various ways, as long as $a(t,t)=1$ and $b(t,t)=0$ hold:

Euler Solver: $f_\theta(x,t,s)=x+(s-t)\mathrm{NN}_\theta(x,t,s)$

Triangular, Linear: omitted

---

Take $w_v(t,\mathrm{MSE_\mathrm{Loss}})=\dfrac{1}{\vert b_2^\prime(t,t)\vert (\mathrm{MSE_\mathrm{Loss}}+\epsilon)^p}$.

The term $\lvert b_2^\prime(t,t)\rvert$ is from $
f_{\theta3}^\prime(x,t,t)=
a_2^\prime(t,t)x+b_2^\prime(t,t)\mathrm{NN_{\theta}}(x,t,s)+b_2(t,t)\mathrm{NN_{\theta2}}^\prime(x,t,s)=a_2^\prime(t,t)x+b_2^\prime(t,t)\mathrm{NN}_{\theta}(x,t,s)=v(x,t)$ (the partial derivative of the second variable).

Take $w_c(t,s,\mathrm{MSE_\mathrm{Loss}})=\dfrac{t-l}{\vert b(t,s)\vert (\mathrm{MSE_\mathrm{Loss}}+\epsilon)^p}$.

_sub iudice_: $\frac{t-l}{\vert b(t,s)\vert }$ is used to balance the gradient scale in $\frac{1}{D}\left\lVert\frac{f_\theta(x,t,s)-f_{\theta^-}(x+v(x,t)(l-t),l,s)}{t-l}\right\rVert_2^2$

---

Our model is also compatible with Classifier-Free Guidance:

We only need to replace the sample-based class-conditioned velocity $v_c(x,t)$ with the following guidance velocity field: $v_g(x,t)=m(v_c(x,t)+(w-1)(v_c(x,t)-f_{\theta3}^\prime(x,t,t,\phi)))+(1-m)f_{\theta3}^\prime(x,t,t,c)$, where

$m\in(0,1]$ is the mix ratio of guidance field and learned guidance field (could reduce target variance),\\
$w\geq 1$ is the guidance strength,\\
$\phi$ is the empty label,\\
$f_{\theta3}^\prime(x,t,t,\phi)$ is the learned unconditional velocity field.

$w=1+(w_0-1)f(t)$, where $f(t)=1,t\leq t_0;1-e^{-k(1-t)/(t-t_0)},\text{otherwise}$ is a scaling function with differentiability to decrease the guidance strength for higher noise level (t is close to 1).

## Experiment Results

| Method | Params | $\mathrm{FD_{PaSST}}\downarrow$ | $\mathrm{FD_{PANNs}}\downarrow$ | $\mathrm{FD_{VGG}}\downarrow$ | $\mathrm{KL_{PANNs}}\downarrow$ | $\mathrm{KL_{PaSST}}\downarrow$ | $\mathrm{IS}\uparrow$ | $\mathrm{IB\text{-}score}\uparrow$ | $\mathrm{DeSync}\downarrow$ | $\mathrm{Time~(s)}\downarrow$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ReWaS | 619M | 141.38 | 17.54 | 1.79 | 2.87 | 2.82 | 8.51 | 14.82 | 1.062 | 15.97 |
| Seeing&Hearing | 415M | 219.01 | 24.58 | 5.40 | 2.26 | 2.30 | 8.58 | 33.99 | 1.204 | 14.55 |
| V-AURA | 695M | 218.50 | 14.80 | 2.88 | 2.42 | 2.07 | 10.08 | 27.64 | 0.654 | 16.55 |
| VATT | - | 131.88 | 10.63 | 2.77 | 1.48 | 1.41 | 11.90 | 25.00 | 1.195 | - |
| Frieren | 159M | 106.10 | 11.45 | 1.34 | 2.73 | 2.86 | 12.25 | 22.78 | 0.851 | - |
| FoleyCrafter | 1.22B | 140.09 | 16.24 | 2.51 | 2.30 | 2.23 | 15.68 | 25.68 | 1.225 | 1.67 |
| V2A-Mapper | 229M | 84.57 | 8.40 | 0.84 | 2.69 | 2.56 | 12.47 | 22.58 | 1.225 | - |
| MMAudio-S-16k<br>25steps | 157M | 70.19 | 5.22 | 0.79 | 1.65 | 1.59 | 14.44 | 29.13 | 0.483 | 1.23 |
| MMAudio-L-44k<br>25steps | 1.03B | 60.60 | 4.72 | 0.97 | 1.65 | 1.40 | 17.40 | 33.22 | 0.442 | 1.96 |
| BiTCAM-S-16k<br>1step | 157M | - | - | - | - | - | - | - | - | - |
| BiTCAM-S-16k<br>4steps | 157M | - | - | - | - | - | - | - | - | - |
| BiTCAM-L-16k<br>1step | 1.03B | 160.71 | 15.25 | 2.59 | 1.89 | 1.89 | 8.15 | 19.36 | 0.913 | - |
| BiTCAM-L-16k<br>4steps | 1.03B | 105.66 | 7.36 | 1.46 | 1.60 | 1.58 | 12.15 | 26.05 | 0.843 | - |

<table><thead><tr>
<td align="center"><b>Ground Truth</b></td>
<td align="center"><b>BiTCAM-L-16k 4steps</b></td>
<td align="center"><b>BiTCAM-L-16k 1step</b></td>
<td align="center"><b>MMAudio-L-44k 25steps</b></td>
</tr></thead><tbody>

<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> child speech, kid speaking</span>
<div class="video-row">
<video controls>
<source src="video/gt/0B4dYTMsgHA_000130.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/0B4dYTMsgHA_000130.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/0B4dYTMsgHA_000130.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/0B4dYTMsgHA_000130.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> whale calling</span>
<div class="video-row">
<video controls>
<source src="video/gt/F8Zt3mYlOqU_000094.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/F8Zt3mYlOqU_000094.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/F8Zt3mYlOqU_000094.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/F8Zt3mYlOqU_000094.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> playing marimba, xylophone</span>
<div class="video-row">
<video controls>
<source src="video/gt/-WIDMrHskbI_000350.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/-WIDMrHskbI_000350.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/-WIDMrHskbI_000350.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/-WIDMrHskbI_000350.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> shot football</span>
<div class="video-row">
<video controls>
<source src="video/gt/0mkj5A9qg9A_000086.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/0mkj5A9qg9A_000086.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/0mkj5A9qg9A_000086.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/0mkj5A9qg9A_000086.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> people eating noodle</span>
<div class="video-row">
<video controls>
<source src="video/gt/0n-Z2AQCRnU_000385.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/0n-Z2AQCRnU_000385.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/0n-Z2AQCRnU_000385.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/0n-Z2AQCRnU_000385.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> helicopter</span>
<div class="video-row">
<video controls>
<source src="video/gt/edObQJBoSPU_000060.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/edObQJBoSPU_000060.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/edObQJBoSPU_000060.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/edObQJBoSPU_000060.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> raining</span>
<div class="video-row">
<video controls>
<source src="video/gt/1XO0SqsZhHU_000030.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/1XO0SqsZhHU_000030.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/1XO0SqsZhHU_000030.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/1XO0SqsZhHU_000030.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>
<tbody><tr><td colspan="4">
<span style="display:block; text-align:left;"><b>Prompt:</b> mouse clicking</span>
<div class="video-row">
<video controls>
<source src="video/gt/TOUHOWRpQYA_000230.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k/TOUHOWRpQYA_000230.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/BiTCAM_L_16k_1step/TOUHOWRpQYA_000230.mp4" type="video/mp4">
</video>
<video controls>
<source src="video/MMAudio_L_44k/TOUHOWRpQYA_000230.mp4" type="video/mp4">
</video>
</div>
</td></tr></tbody>

{% raw %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
{% endraw %}
