---
title: "Roads Centre-axis extraction in aiorborne SAR images: an approach based on active contour model with the use of semi-automatic seeding"
venue: "ISPRS Hannover, Germany, 2013"
date: 2013-05-21
classes: wide
layout: archive
categories:
  - proceedings
tags:
  - active-contour
  - road extraction
  - kohonen
  - sar  
---
<span style="color:lightblue">**Rodolfo G. Lotte**</span>, Sidnei J. S. Sant'Anna, Cláudia M. Almeida

[<i class='fas fa-file-download'></i> Download paper](/assets/files/publications/isprs-2013/isprs-2013.pdf){: .btn .btn--danger}
[<i class='fas fa-file-download'></i> Download poster](/assets/images/papers/isprs-2013/isprs-2013.png?style=padme){: .btn .btn--success}

Abstract
======
<h-abstract>The reasearch dealing with computational methods for roads extraction have considerably increased in the latest two decades. This procedure is usually performed on optical or microwave sensors (radar) imagery. Radar images offer advantages when compared to optical ones, for they allow the acquisition of scenes regardless of atmospheric and illumination conditions, besides the possibility of surveying regions where the terrain is hidden by the vegetation canopy, among others. The cartographic mapping based on these images is often manually accomplished, requiring considerable time and effort from the human interpreter. Maps for detecting new roads or updating the existing roads network are among the most important cartographic products to date. There are currently many studies involving the extraction of roads by means of automatic or semi-automatic approaches. Each of them presents different solutions for different problems, making this task a scientific issue still open. One of the preliminary steps for roads extraction can be the seeding of points belonging to roads, what can be done using different methods with diverse levels of automation. The identified seed points are interpolated to form the initial road network, and are hence used as an input for an extraction method properly speaking. The present work introduces an innovative hybrid method for the extraction of roads centre-axis in a synthetic aperture radar (SAR) airborne image. Initially, candidate points are fully automatically seeded using Self-Organizing Maps (SOM), followed by a pruning process based on specific metrics. The centre-axis are then detected by an open-curve active contour model (snakes). The obtained results were evaluated as to their quality with respect to completeness, correctness and redundancy.</h-abstract>

**Info!** Dear researcher/scientist/academic, you may find some Wikipedia references in this page, which are totally directed for those that might not be familiar with terms and need a more illustrative and didatical understanding. Please, fell free to contribute at any moment. 
{: .notice--warning}

Contextualization
======

<!-- O propósito básico deste trabalho foi a extração automática de redes de estradas e da investigação quanto a possibilidade de aplicação de Modelos de Contorno Ativo (de curvas aberto) sobre imagens SAR (Synthetic Aperture Radar), cuja visibilidade topográfica sobre regiões recobertas por copas de árvores ou núvens é alta. Isto aumenta o poder de investigação sobre áreas em que há estradas ilegais, por exemplo, para contrabando de mercadorias, trafico de drogas, assentamentos ilegais, etc.  -->
The basic purpose of this work was the automatic extraction of road networks and the investigation of the possibility of applying Active Contour Models (open curves) on SAR (Synthetic Aperture Radar) images, whose topographic visibility on regions covered by treetops or clouds is high. This increases the power of investigation on areas where there are illegal roads, for example, for goods smuggling, drug trafficking, illegal settlements, etc.

<!-- Modelos de contorno ativo, ou comumente chamados de Snakes, são modelos não paramétricos ou simplesmente uma técnica em Visão Computacional, tal que dado alguns pontos iniciais sobre uma imagem digital, uma curva é então definida sobre esses pontos. A medida em que o método é aplicado, os pontos (consequentemente a curva) são movidos em direção à regiões em que haja diferenças de contrastes (bordas). Ao final do processo, a curva que inicialmente estava sobre qualquer região da imagem, é então posicionada perfeitamente sobre a curva mais próxima. -->
Active Contour Models [[1]](http://www.cs.ait.ac.th/~mdailey/cvreadings/Kass-Snakes.pdf), or commonly called Snakes (an informal and more didatic explanation can be found [here](https://en.wikipedia.org/wiki/Active_contour_model)), are non-parametric models or simply a technique in Computational Vision, such that given some initial points on a digital image, a curve is then defined on those points. As soon as the method is applied, the points (hence the curve) are moved toward regions where there are high differences in contrast (edges) - gradient. At the end of the process, the curve that was initially on any region of the image, is then positioned perfectly on the closest object, more specificaly, on its contour. 

<!-- Sabendo-se disso, é razoável imaginar que a posição dos pontos iniciais que formam a curva, precisam necessariamente localizar-se em um regiões mais próximas possível do objeto de interesse. Quanto mais próximo do alvo, mais rápido será o processo de minimização. Portanto, a escolha dos pontos iniciais é realizada de forma inteligente neste trabalho. Com o uso de um método de clusterização, denominado Mapas Auto-Organizáveis ou Mapas de Kohonen [CITE], os pontos iniciais para aplicação do Modelo de Contorno Ativo são dispostos o mais próximo possíveis de estradas, caracterizadas em imagens SAR por feições lineares, ora com brilho muito intenso (não pavimentas), ora escuras (pavimentadas). -->
Knowing this, it is reasonable to imagine that the position of the initial points forming the curve must necessarily be located in a region as close as possible to the object of interest. The closer the target, the faster the minimization process. Besides, the location of the starting-points are also essential, for instance, see the Lecture below, gave by Rich Radke, which gives a bit more explanatory example about closed-curve Snakes - 35min50sec). 

{% include video id="RJEMDkhVgqQ" provider="youtube" %}

Therefore, assuming the location of the starting-points a crutial requisite, the choice of them is performed intelligently in this work. With the use of a clustering method, called [Kohonen Maps](https://link.springer.com/article/10.1007%2FBF00337288) (wikipedia explanation [here](https://en.wikipedia.org/wiki/Self-organizing_map)), the starting points for the application of the Active Contour Model are as close as possible to roads, characterized in SAR images by linear features, sometimes, with very intense brightness (not paved), sometimes dark (paved).

The recognition by the use of SOM methodology was not so efficient when the presence of noisy was applenty. The training samples should have much more examples and take iterations. The experiments were taken over synthetic and real SAR images, as it can be seen below:

![alt-Synthetic SAR image and the starting-points before and after Snakes.](/assets/images/papers/isprs-2013/result1.png?style=centerme)
*Synthetic SAR image and the starting-points before and after Snakes* 
{: .image-caption}

![alt-SAR image and the starting-points before and after Snakes.](/assets/images/papers/isprs-2013/result2.png?style=centerme)
*SAR image and the starting-points before and after Snakes* 
{: .image-caption}

To minimize this effect was created pruning algorithm, which allowed the choice of the best points among those identified, eliminating the others. Thus, many of the spurious points are eliminated and hence more concise hypotheses are selected from line segments. It is noted for the final results of extraction that seeding directly influences the quality of final results. Due to the characteristics of the image, identification of a particular pattern be
comes a difficult task and the seeding process often comes to errin its determinations. The experiment conducted with the synthetic image shows the efficiency of the Snakes method when the seeds points are marked near road, mostly, converging exactly to the central axis of the roads.

Source-code and tools
======
The tools and source-code was mainly made in MATLAB, which a set of scripts (.m) were used to train the SOM model with 21 specific road patterns, then, the SAR images are loaded to convolve over every part of the image, with this, parts that are too similar compared to the training samples, a seed "planted up". ENVI was used to configure the training samples by the transect tool. For documentation, the LaTeX and Kile editor were used. Below, each tool is presented as an icon, together with its frequency of use.

**Coding:**

| ![alt-MATLAB](/assets/images/logo/same-dim/matlab.png?style=centerme) | 
|:--:|
| MATLAB | 
|:--:|
|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|

**IDE:**

| ![alt-PyCharm](/assets/images/logo/same-dim/envi.png?style=centerme) | ![alt-PyCharm](/assets/images/logo/same-dim/netbeans.png?style=centerme) | 
|:--:|:--:|
| ENVI | Netbeans |
|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:red"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|

**Arts:**

| ![alt-Adobe Illustrator](/assets/images/logo/same-dim/illustrator.png?style=centerme) | ![alt-Adobe Photoshop](/assets/images/logo/same-dim/photoshop.png?style=centerme) |
|:--:|:--:|
| Illustrator | Photoshop |
|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|

**Documentation:**

| ![alt-Kile](/assets/images/logo/same-dim/kile.png?style=centerme) | ![alt-LaTeX](/assets/images/logo/same-dim/tex.png?style=centerme) |
|:--:|:--:|
| Kile | LaTeX |
|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|


Presentation
======
![image-left](/assets/images/papers/isprs-2013/isprs-2013-thumb.png){: .align-left} This work has been presented in a poster form (left), during the [International Society for Photogrammetry and Remote Sensing (ISPRS)](www.isprs.org/), hosted by the Department of Photogrammetry (IPI) of the University of Hannover, in Germany, 2013. The poster can be download in the green buttom at the top of this page.

For this presentation, we summarized the stages since the raw SAR image until the delineation of the roads network by the use of Active Contour, which is initializated by points recognized by Self-Organized Maps.

Still, the results show the difficult on the application of Snakes over too noisy images. The model should to include a weight that would aldo take into account the speckle noisy, which would allow to compensate the evolution on the energy function minimization. 

Cite this paper
======

```latex
@article{lotte2013-isprs,
  title={Roads Centre-Axis Extraction in Airborne SAR Images: AN Approach Based on Active Contour Model with the Use 
  of Semi-Automatic Seeding},
  author={Lotte, RG and Sant'Anna, SJS and Almeida, CM},
  journal={ISPRS-International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences},
  number={1},
  pages={207--212},
  year={2013}
}
```

References
======
1. Kass, Michael, Andrew Witkin, and Demetri Terzopoulos. [Snakes: Active contour models](http://www.cs.ait.ac.th/~mdailey/cvreadings/Kass-Snakes.pdf). International journal of computer vision 1.4 (1988): 321-331.
2. Kohonen, Teuvo (1982). [Self-Organized Formation of Topologically Correct Feature Maps](https://link.springer.com/article/10.1007%2FBF00337288). Biological Cybernetics. 43 (1): 59–69. DOI: 10.1007/bf00337288



