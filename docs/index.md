---
layout: default
---

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
