---
layout: default
---

<link rel="stylesheet" href="/assets/css/custom.css">

$\mathrm{}$

IS_PANNs

| Method | Params | $\mathrm{FD_{PaSST}}\downarrow$ | $\mathrm{FD_{PANNs}}\downarrow$ | $\mathrm{FD_{VGG}}\downarrow$ | $\mathrm{KL_{PANNs}}\downarrow$ | $\mathrm{KL_{PaSST}}\downarrow$ | $\mathrm{IS}\uparrow$ | $\mathrm{IB\text{-}score}\uparrow$ | $\mathrm{DeSync}\downarrow$ | $\mathrm{Time~(s)}\downarrow$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MMAudio-S-16k-25steps | 157M | 70.19 | 5.22 | 0.79 | 1.65 | 1.59 | 14.44 | 29.13 | 0.483 | 1.23 |
| MMAudio-L-44k-25steps | 1.03B | 60.60 | 4.72 | 0.97 | 1.65 | 1.40 | 17.40 | 33.22 | 0.442 | 1.96 |
| BiTCAM-S-16k-1step
| BiTCAM-S-16k-4steps
| BiTCAM-L-16k-v2-1step | | 160.71 | 15.25 | 2.59 | 1.89 | 1.89 | 8.15 | 19.36 | 0.913 | |
| BiTCAM-L-16k-v2-4steps | | 105.66 | 7.36 | 1.46 | 1.60 | 1.58 | 12.15 | 26.05 | 0.843 | |

<video width="640" height="360" controls>
    <source src="audio/__2MwJ2uHu0_000004.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<video src="audio/__2MwJ2uHu0_000004.mp4" controls width="640" height="360"></video>

<video width="1280" height="720" controls autoplay muted loop>
<source src="audio/__2MwJ2uHu0_000004.mp4" type="video/mp4">
 Your browser does not support the video tag.
</video>

<video width="1280" height="720" controls autoplay>
<source src="video/TOUHOWRpQYA_000230.mp4" type="video/mp4">
 Your browser does not support the video tag.
</video>



<table><thead><tr><td align="center"><b>Ground</b><br><b>Truth</b></td>
<td align="center"><b>WaveFM</b><br><b>(6 steps)</b></td>
<td align="center"><b>WaveFM</b><br><b>(1 step)</b></td>
<td align="center"><b>BigVGAN-base</b><br><b>(1 step)</b></td>
<td align="center"><b>PriorGrad</b><br><b>(6 steps)</b></td>
<td align="center"><b>DiffWave</b><br><b>(6 steps)</b></td>
<td align="center"><b>HifiGAN-V1</b><br><b>(1 step)</b></td>
<td align="center"><b>FreGrad</b><br><b>(6 steps)</b></td>
<td align="center"><b>FastDiff</b><br><b>(6 steps)</b></td></tr></thead><tbody>
<tbody><tr><td colspan="9">MUSDB18-HQ Mixture 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><video id="player" controls preload="auto"><source src="audio\__2MwJ2uHu0_000004.mp4"></video></td>
<td align="center"><audio id="player" controls style="width:100px;" preload="auto"><source src="audio\1188_133604_000018_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\BigVGAN-base_(1_step)\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\PriorGrad_(6_steps)\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\DiffWave_(6_steps)\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\HifiGAN-V1_(1_step)\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\FreGrad_(6_steps)\Actions_-_South_Of_The_Water.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\FastDiff_(6_steps)\Actions_-_South_Of_The_Water.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Mixture 6</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Young_Griffo_-_Facade.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Bass 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Actions_-_Devil's_Words.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Drum 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Leaf_-_Summerghost.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Vocal 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Flags_-_54.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Vocal 2</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\The_Wrong'Uns_-_Rothko.wav"></audio></td>

</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Vocal 3</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Bill_Chudziak_-_Children_Of_No-one.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">MUSDB18-HQ Others 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\Fergessen_-_Nos_Palpitants.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 1</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\84_121123_000015_000000.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 2</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\174_168635_000024_000001.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 3</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\1188_133604_000018_000000.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 4</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\1272_135031_000054_000000.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 5</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\2277_149896_000023_000001.wav"></audio></td>
</tr></tbody><tbody><tr><td colspan="9">LibriTTS Test 6</td></tr></tbody><tbody><tr>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\Ground_Truth\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\WaveFM_(6_steps)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\WaveFM_(1_step)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\BigVGAN-base_(1_step)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\PriorGrad_(6_steps)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\DiffWave_(6_steps)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\HifiGAN-V1_(1_step)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\FreGrad_(6_steps)\3538_163624_000015_000000.wav"></audio></td>
<td align="center"><audio id="player" controls="" style="width:100px;" preload="auto"><source src="audio\FastDiff_(6_steps)\3538_163624_000015_000000.wav"></audio></td>
</tr></tbody>

{% raw %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
{% endraw %}
