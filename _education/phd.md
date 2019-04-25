---
title: "3-dimensional (3D) urban mapping: A study of detection and reconstruction of building's facade through Structure-from-Motion (SfM) and Convolutional Neural Network (CNN)"
layout: archive
classes: wide
author_profile: true
---
[<i class='fas fa-file-download'></i> Download thesis](http://urlib.net/rep/8JMKD3MGP3W34R/3RKQRSE){: .btn .btn--danger}
[<i class='fas fa-file-download'></i> Download defense](https://www.dropbox.com/s/t64tx0qsqzoq9hn/defense.pdf){: .btn .btn--warning}
[<i class='fas fa-file-download'></i> Related paper](https://www.mdpi.com/2072-4292/10/9/1435/pdf){: .btn .btn--info}

<!-- Resumo
======
Ambientes urbanos são regiões cuja variabilidade espectral e espacial é extremamente alta, com uma enorme variedade de formas e tamanhos que remetem igualmente ao sensoriamento remoto de alta resolução em aplicações envolvendo seus estudos. Devido ao fato de que esses ambientes podem crescer ainda mais, as aplicações relacionadas ao seu monitoramento em larga escala tendem a recorrer a sistemas autônomos que, juntamente com imagens de alta resolução, podem ajudar e até predizer situações cotidianas. Aliado à detecção inteligente dessas feições, representações 3D desses ambientes têm sido também objeto de estudo ao auxiliar na investigação da qualidade ambiental de áreas muito densas, padrões socioeconômicos de ocupação, na construção de modelos de paisagem urbanos, avaliação de efeitos de ilhas de calor, demolições de edifícios ou simulações de inundações para planos de evacuação e delimitação estratégica, entre inúmeros outros. Por estes aspectos, o objetivo desta pesquisa de doutorado foi explorar as vantagens de tais tecnologias, de forma a apresentar não só uma metodologia automática para detecção e reconstrução de elementos urbanos, como também compreender as dificuldades que ainda cercam o mapeamento automático desses ambientes. Como objetivos específicos: (i) Desenvolver uma rotina de classificação automática de feições de fachadas no domínio 2D, utilizando-se de uma Rede Neural Convolutiva (CNN). (ii) Com as mesmas imagens, obter a geometria da fachada pelas técnicas de Estrutura por Movimento (em inglês, \emph{Structure-from-Motion} (SfM)) e Estéreo por Multi-Visadas (em inglês, \emph{Multi-View Stereo} (MVS)). (iii) Avaliar o desempenho do modelo neural para diferentes cenários urbanos e estilos arquitetônicos. (iv) Avaliar o desempenho do modelo neural em uma aplicação real no Brasil, cuja arquitetura diferencia-se dos dados utilizados no treinamento do modelo neural. (v) Classificar o modelo 3D da fachada extraída utilizando-se das imagens segmentadas no domínio 2D pela técnica de \emph{Ray-Tracing} (RT). Para tanto, a metodologia do trabalho foi dividida em análise 2D (detecção) e 3D (reconstrução). De forma que no primeiro, uma CNN supervisionada é utilizada para segmentar imagens ópticas terrestres de fachadas em seis classes: telhado, janela, parede, porta, sacada e lojas. Simultaneamente, a fachada é reconstruída pelo uso do \emph{pipeline} SfM/MVS, obtendo-se a geometria da cena. Por fim, os resultados da segmentação no domínio 2D, juntamente com 3D, são então vinculados pela técnica de RT, obtendo-se finalmente o modelo 3D classificado. É demonstrado que a metodologia proposta é robusta em relação a cenários complexos. As inferências realizadas com o modelo neural CNN alcançou até 93\% de acurácia, e 90\% de F1-score para maioria dos conjuntos de dados utilizados. Para cenários desconhecidos, o modelo neural atingiu índices de acurácia inferiores, justificado pela elevada diferenciação de estilos arquitetônicos. Contudo, a utilização de modelos neurais \emph{deep}, dão margem à novas configurações e uso conjunto com outras arquiteturas \emph{deep} para a melhoria dos resultados, sobretudo, aos modelos não-supervisionados. Por fim, o trabalho demonstrou a capacidade autônoma de uma Rede Neural Convolutiva frente a complexidade dos ambientes urbanos, de modo a diversificar entre diferentes estilos de fachadas. Embora haja melhorias a serem realizadas quanto à classificação 3D, a metodologia é consistente e permitiu aliar métodos de última geração na detecção e reconstrução de fachadas, além de fornecer suporte à novos estudos e projeções sobre cenários ainda mais distintos. -->

Abstract
======
<h-abstract>Urban environments are regions in which spectral and spatial variability are extremely high, with a huge range of shapes and sizes, they also demand high resolution images for applications involving their study. These environments can grow over time, applications related to their large-scale monitoring tend to rely on autonomous intelligent systems that, along with high-resolution images, can help and even predict everyday situations. In addition to the detection of these features, 3D representations of these environments have also been object of study to assist in the investigation of the environmental quality of very dense areas, occupational socioeconomic patterns, the construction of urban landscape models, building demolitions or flood simulations for evacuation plans and strategic delimitation, among countless others. The main objective of this study was to explore the advantages of such technologies, in order to present an automatic methodology for the detection and reconstruction of urban elements, and also to understand the difficulties that still surround the automatic mapping of these environments. Specifically we aimed: (i) To develop a routine of automatic classification of facade features in 2D domain, using a Convolutional Neural Network (CNN); (ii) Using the same images, obtain the facade geometry using Structure-from-Motion (SfM) and Multi-View Stereo (MVS) techniques; (iii) Evaluate the performance of the CNN for different urban scenarios and architectural styles; (iv) Evaluate the performance of the CNN in a real application in Brazil, whose architecture differs from the datasets used in the neural model training; and (v) Classify the 3D model of the extracted facade using images segmented in 2D domain by the Ray-Tracing (RT) technique. In order to atempt that, the methodology was splited into 2D analysis (detection) and 3D (reconstruction). So in the first, a supervised CNN is used to segment terrestrial optical images of facades into six classes: roof, window, wall, door, balcony and shops. At the same time, the facade is reconstructed using the SfM/MVS technique, obtaining the geometry of the scene. Finally, the results of segmentation in both domains, 2D and 3D, are then merged by the Ray-Tracing technique, finally obtaining the 3D model classified. It is demonstrated that the proposed methodology is robust toward complex scenarios. The inferences made with the CNN reached up to 93% accuracy, and 90% F1-score for most of the datasets used. For scenarios not used for training, the neural model reached lower accuracy indexes, justified by the high differentiation of architectural styles. However, the use of deep neural models gives chances for new configurations and use with other deep architectures to improve results, especially for unsupervised models. Finally, the work demonstrated the autonomous capacity of a CNN against the complexity of urban environments, in order to diversify between different styles of facades. Although there are improvements to be made regarding 3D classification, the methodology is consistent and allowed to combine state-of-the-art methods in the detection and reconstruction of urban elements, as well as providing support for new studies and projections on even more distinct scenarios.</h-abstract>

**Info!** Dear researcher/scientist/academic, you may find some Wikipedia references in this page, which are totally directed for those that might not be familiar with terms and need a more illustrative and didatical understanding. Please, fell free to contribute at any moment. 
{: .notice--warning}

Contextualization
======
A 3-dimensional (3D) representation of cities became a common term in the last decade. What was once considered an alternative for visualization and entertainment, has become a powerful instrument of urban planning. The technology is now well-known in most of the countries on the European continent, such as [Switzerland](https://www.swisstopo.admin.ch/), England ([AccuCities](https://www.accucities.com/) and [Vertex Modelling](http://vertexmodelling.co.uk/3d-models-products/london-3d-model/)), [Germany](https://berlin.virtualcitymap.de/), finally, [Netherlands](https://github.com/tudelft3d/3dfier), and other. Also being commercially popular in North America, where many leading companies and precursor institutions reside. However, the semantic 3D mapping with features and applicability that go beyond the visual scope, is still considered a novelty in many other countries. In Brazil, according to the present study, the use of volumetric information as a resource for strategic and management planning is reduced to few cities.

<!-- O desafio em mapear e, consequentemente, monitorar perímetros urbanos é uma tarefa difícil quando direcionada em escalas maiores. Cidades ainda possuem a características de se alterarem constantemente, são ambientes dinâmicos, de constrastes, formas e tamanhos infinitos, que podem maximizar a capacidade de pessoal especializado em tarefas envolvendo sua gestão. Dentre essas áreas, as engenharias, civil, cartográfica, geodésica, na arquitetura, urbanismo, dentre outras.  -->
The challenge of mapping and monitoring urban environments is a tough task, specially when apply under larger scales. Cities are dynamic environments, with a huge amount of shapes, sizes, the constant action of man, the presence of cars, vegetation, vehicles and pedestrians aggravate the extraction of key informations, which maximize the especialist capacity to handle tasks that involves their management. 

However, not all cities are that chaotic. One city could present a better geometry when compared to another in terms of architectural styles, for example, the streets of Manhattan (wide), in United States, and the streets of Hong Kong (narrow), in China. In addition, suburbs use to have less traffic than city-centers, and that also affects the extraction. The term "complex" in this study refers to images where no preprocessing is performed, no cars are removed, no trees are cut off to benefit the imaging, no house or street was chosen beforehand, only images representing the perfect register of a real chaotic scenario were taken.

<!-- Atualmente, as soluções e recursos (ferramentas) disponíveis para o mapemanto sistemático e volumétrico de cidades, variam entre sensores de imageamento sofisticados e ferramentas computacionais de ponta, que visam usufruir dos dados imageados da maneira mais otimizada possível.  -->
Currently, the solutions and resources available for systematic and volumetric mapping of cities, vary among the components of sophisticated imaging and computational tools, which aims to explore the imaged data in the most optimized way as possible.

This work was based on the following **hypotheses**:
  1. The volumetry of buildings, as well as their facade features (e.g. roof, windows, balconies, wall and doors), can be accurately extracted through optical images and SfM/MVS technique;           
  2. Facade features can be automatically detected with CNN even under complex scenarios with no preprocessing need;    
  3. The geometric quality of the 3D model, as well as the quality of the 3D labeling, is a direct function of the point cloud density;  
  4. The geometric quality point cloud by SfM/MVS technique depends on the camera parameter estimation, image spectral and spatial characteristics. Therefore, the targets geometry and texture are fundamental in the process of reconstruction and classification.      

followed by the main **objective**:

## *From structural data campaigns (image-based point cloud), the main objective of this research is to explore the extraction of geometric information of buildings, simultaneously, to detect their facade features and, finally, relate both information in one single 3D labeled model.*

and specifically:
  1. Develop a routine to classify facade elements in 2-dimensional (2D) images using a CNN architecture;
  2. Using the same images, obtain the facade geometry using SfM/MVS;
  3. Evaluate the performance of the neural model for different urban scenarios and architectural styles;
  4. Evaluate a case study with an application in Brazil, whose architecture differs from the datasets used during the neural model training;
  5. Classify the 3D model of the extracted facade using the images previously segmented in the 2D domain by the technique of Ray-Tracing. 

Methodology
======
The complete methodology of this case study, as shown in Figure below, consists of three stages: A supervised CNN model for semantic segmentation (blue); Scene geometry acquirement (3D reconstruction) through SfM and MVS pipeline (red); Post-processing procedures (yellow); and 3D labeling through ray-tracing analysis (white). The boxes in gray represent the products, delivered in different steps of the workflow.

![image-center](/assets/images/phd/methodology/methodology.png){: .align-center}
*Methodology* 
{: .image-caption}

In summary, the first part comprises two paralell procedures: the applicability of Structure-from-Motion (SfM) and the Deep-Learning (DL) facade features training. The first one, takes into account the extraction of volumetry information from the facades. Once the geometry is extracted, characteristics such as shape, size, the many spare balconies, among others, complement more detailed analysis. However, the geometry itself can't say much to sistematic analysis of buiding facades. It needs to have labels! It needs to have classified features for each of its geometry. In this sense, the DL complements with his ability to detect patterns under 2D images. Both extracted information: 3D (facade geometry) + 2D (facade features classified), integrates the outcomes of this methodogical stage.



{% include video id="H-CMDCmehy4" provider="youtube" %}

Results
======
The DL source-code was mainly developed under the [Tensorflow library](https://www.tensorflow.org/) and adjusted to the problem together with other Python libraries. Except for the 3D tasks in [Agisoft Photoscan](https://www.agisoft.com/), the source-code are freely available in a public platform, and can be easily extended. For training and inferences, it was used an Intel Xeon CPU E5-2630 v3@2.40GHz. For SfM/MVS and 3D labeling, respect to RueMonge2014 and SJC datasets, it was used an Intel Core i7-2600 CPU@3.40GHz. Both attended our expectations, but it is strongly recommended machines with GPU support or alternatives such as IaaS (Infrastructure as a Service).

The Figure below shows the inferences from [Ruemonge2014](https://varcity.ethz.ch/3dchallenge/) dataset over the validation set. Instead of showing only a few example results, they were exposed as much as possible to allow the reader to better understand how the neural model behaves according to different situations. Here, it is positively highlighted two aspects. First, the robustness of the neural model in the detection of facade features even under shadow or occluded areas, such as in the presence of pedestrians or cars. This aspect has been one of the most difficult issue to overcome due to the respective obstacles being dynamic and difficult to deal with, especially by the use of pixelwise segmenters. The second aspect is that at 50 thousand (k) iterations, all images presented fine class delineation. Only in a few situations the inferences were not satisfactory. 

![image-center](/assets/images/phd/results/2d/ruemonge.PNG){: .align-center}

|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) | (i) | (j) |

*Results over [Ruemonge2014](https://varcity.ethz.ch/3dchallenge/). The rows are splited respectively in original, segmented image, and both. These segmented images are the inferences under evaluation sets only. (a)--(j) Example of RueMonge2014 images, segmented by the neural model presented. In the first row, the original image, the second row, the result of the inference (segmentation), and the third and last, the overlapping images.*
{: .image-caption}

The quality of the reconstructed surface (mesh) is highly dependent on the density of the point cloud and the method of reconstruction. Very sparse point clouds can generalize feature volumetry too much, while very dense point clouds can represent it faithfully, but the associated computational cost will also increase. Therefore, there is a limit between the quality of the 3D labeled model and the point cloud density, which falls on the question: how many points it is needed to fairly represent a specific feature? 

Features that are segmented in 2D domain might perfectly align with their geometry, but imprecisions between the geometric edges and the classification may occur. Despite of that, the segmentation alignment onto the mesh is also related to the estimated camera parameters, which are used during ray-tracing. These impressions are directly related to the mesh quality. 

![image-center](/assets/images/phd/results/3d/ruemonge.png){: .align-center}
*3D labeled model of RueMonge2014. Wide view of the street, facade geometry and its labels after ray-tracing analysis*
{: .image-caption}

Considerations
======
Increasingly, the research regarding the facade feature extraction from complex structures, under a dynamic and hard-to-work environment (crowded cities) represent a new branch of research, with perspectives to the areas of technology, such as the concept of smart cities, as well as the areas of Cartography, toward to more detailed maps and semantized systems. In this study, an overview of the most common techniques was presented, as well as an introduction of instruments and ways of observing structural information through remote sensing data. Besides, was also presented a methodology to detect facade features by the use of a CNN, incorporating this detection to its respective geometry through the application of a SfM pipeline and ray-tracing analysis. 

The experiments are mainly focused in aspects such those aforementioned techniques and their computational capability in detecting facade features, regardless of architectural style, location, scale, orientation or color variation. All the images used in the training procedures underwent no preprocessing whatsoever, keeping the study area as close as possible as to what would be a common-user dataset (photos taken from the streets). 

In this sense, the edges of the acquired delineated features show the robustness of the CNN technique in segmenting any kind of material, in any level of brightness (shadow and occluded areas), orientation, or presence of pedestrians and cars. Considering that the values achieved for the individual datasets were above 90%, it is concluded that the CNNs can provide good results for image segmentation in many situations. However, being a supervised architecture, the network has to pass through a huge training set, with no guarantees of good inputs, in order to get reliable inferences. When applied over unknown data, such as the experiment on the SJC data, it was noted that the neural network failed, except in regions where the facade features share similar characteristics, though such occasions were rare.

Identifying facade features under a great variety and arrangement make up these tasks still a scientific challenge whose tendency is to expand. The technologies to observe cities, such as sophisticated sensors, reconstruction and classification techniques, evolve as the numerous architectural styles change according to local culture and way of life. Moreover, it is essential to think that the multiplicity of architectural styles is not the only problem. Studies, such as those carried out at the MIT Center for Art, Science and Technology (CAST), [Massachusetts Institute of Technology (MIT)](https://www.youtube.com/watch?v=vRfNbhyPPKs) and at [Eidgenössische Technische Hochschule (ETH)](https://www.ethz.ch/de.html) Zürich, show, for example, that materials used in construction might become dynamic and therefore do not present a single static structure of a building. Urban occupation tends to evolve, which also demands that mapping techniques must both to follow the current architectural structures, as well as their eminent evolution.

Source-code and tools
======
For training and image processing, I use Python coding language and PyCharm IDE for most of the tasks (in this stage, Tensorflow, and common image processing libraries had been adopted). For the ray-tracing processing, the C++ language was used. CGAL and PCL were used during the point-cloud experiments, such as individual points classification, simplification, and geometry analysis. For documentation, the LaTeX and Kile editor were used. Below, each tool is presented as an icon, together with its frequency of use.

**Coding:**

| ![alt-CGAL](/assets/images/logo/same-dim/cgal.png?style=centerme) | ![alt-PCL](/assets/images/logo/same-dim/pcl.png?style=centerme) | ![alt-TensorFlow](/assets/images/logo/same-dim/tensorflow.png?style=centerme) | ![alt-C++](/assets/images/logo/same-dim/cpp.png?style=centerme) | ![alt-Python](/assets/images/logo/same-dim/python.png?style=centerme) |
|:--:|:--:|:--:|:--:|:--:|
| CGAL | PCL | Tensorflow | C++ | Python |
|:--:|:--:|:--:|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:red"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|

**IDE:**

| ![alt-PyCharm](/assets/images/logo/same-dim/pycharm.png?style=centerme) | ![alt-Meshlab](/assets/images/logo/same-dim/cc.png?style=centerme) | ![alt-CloudCompare](/assets/images/logo/same-dim/meshlab.png?style=centerme) | ![alt-Quantum GIS](/assets/images/logo/same-dim/qgis.png?style=centerme) | 
|:--:|:--:|:--:|:--:|
| PyCharm | CloudCompare | Meshlab | QGIS |
|:--:|:--:|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:orange"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|

**Arts:**

| ![alt-Blender](/assets/images/logo/same-dim/blender.png?style=centerme) | ![alt-Adobe Illustrator](/assets/images/logo/same-dim/illustrator.png?style=centerme) | ![alt-Adobe Photoshop](/assets/images/logo/same-dim/photoshop.png?style=centerme) | ![alt-Adobe InDesign](/assets/images/logo/same-dim/indesign.png?style=centerme) | 
|:--:|:--:|:--:|:--:|
| Blender | Illustrator | Photoshop | InDesign |
|:--:|:--:|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:red"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#50ff00"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:yellow"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|<i class="fa fa-ellipsis-h" style="color:red"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i><i class="fa fa-ellipsis-h" style="color:#454D5B"></i>|

**Documentation**

| ![alt-Kile](/assets/images/logo/same-dim/kile.png?style=centerme) | ![alt-LaTeX](/assets/images/logo/same-dim/tex.png?style=centerme) |
|:--:|:--:|
| Kile | LaTeX |
|:--:|:--:|
|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|<i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i><i class="fa fa-ellipsis-h" style="color:#00bfff"></i>|

To exemplify, the `.gif` below, shows an example of the 3D labeled model on Meshlab, which gives all support for processing and visualize either point cloud or 3D mesh format files.

![image-center](/assets/images/phd/results/3d/handling-3d-meshlab.gif){: .align-center}
*Example of a 3D .ply file handled in Meshlab. The animation shows the 3D labeled model of one of the streets used in this work ([Ruemonge2014](https://varcity.ethz.ch/3dchallenge/) dataset), as well as the differences between sparse and dense mesh*
{: .image-caption}

Presentation
======
![image-left](/assets/images/phd/presentation/presentation.png){: .align-left} The defense of the thesis toke place at National Institute for Space Researche (INPE), at 9am, and was composed by the examiners Prof. Dr. Thales Körting (INPE), Prof. Dr. Norbert Haala (IfP-Sttutgart), Prof. Dr. Edson Mitishita (UFPR), Prof. Dr. Antônio Maria G. Tommaselli (UNESP-Prudente), Dr. Fabien H. Wagner (INPE), Dr. Luiz E. O. E. Aragão (INPE-Advisor), and Dr. Yosio E. Shimabukuro (INPE-Advisor).

The presentation was unanimously approved and is available physically and virtual,ly for consults in the collection of INPE library, in São José dos Campos. The direct link for digital source, simply click on the red button above. 

Cite this thesis
======

```latex
@PhDThesis{lottethesis,
               author = "Lotte, Rodolfo Georjute",
                title = "3-dimensional (3D) urban mapping: A study of detection and reconstruction of building's 
                facade through Structure-from-Motion (SfM) and Convolutional Neural Network (CNN)",
               school = "Instituto Nacional de Pesquisas Espaciais (INPE)",
              address = "São José dos Campos",
                month = "2018-08-24",
             keywords = "3D urban mapping, facade features, deep-learning, convolutional 
                         neural network, structure-from-motion.",
            committee = "Aragão, Luiz Eduardo Oliveira e Cruz de and Shimabukuro, 
                         Yosio Edemir and Körting, Thales Sehn and Wagner, Fabien 
                         Hubert and Tommaselli, Antônio Garcia and Mitishita, Edison 
                         Aparecido and Haala, Norbert",
         englishtitle = "Mapeamento urbano tridimensional (3D): Um estudo sobre 
                         detecção e reconstrução de fachadas de 
                         edificações por Estrutura-por-Movimento (SfM) e Redes 
                         Neurais Convolutivas (CNN)",
             language = "en",
                pages = "139"
}
```

References
======
1. AccuCities LTD. [3D Model of London & 3D City Models](http://www.accucities.com). 2017.
2. Adriaenssens, S.; Gramazio, F.; Kohler, M.; Menges, A.; Pauly, M. [Advances in Architectural Geometry 2016](https://vdf.ch/advances-in-architectural-geometry-2016-e-book.html). [S.l.]: vdf Hochschulverlag AG, 2016. ISBN 978-3-7281-3777-7.
3. Bódis-Szomorú, A.; Riemenschneider, H.; Gool, L. V. [Efficient edge-aware surface mesh reconstruction for urban scenes](http://www.vision.ee.ethz.ch/~rhayko/paper/cviu2017_bodis_spmesh2.pdf). Computer Vision and Image Understanding, v. 157, p. 3–24, 2017.
4. Furukawa, Y.; Curless, B.; Seitz, S. M.; Szeliski, R. [Clustering views for multi-view stereo](https://computervisiononline.com/software/1105138497). In: Computer Vision and Pattern Recognition (CVPR). Proceedings... San Francisco, CA, USA: IEEE, 2010. v. 13, p. e18.
5. Furukawa, Y.; Ponce, J. [Accurate, dense, and robust multi-view stereopsis](https://www.di.ens.fr/willow/pdfs/cvpr07a.pdf). In: Computer Vision and Pattern Recognition. Proceedings...Minneapolis, MN, USA: IEEE, 2007. p. 1–8. ISSN 1063-6919.
6. Furukawa, Y.; Ponce, J. [Patch-based multi-view stereo software](https://www.di.ens.fr/pmvs/). 2010.
7. Lecun, Y.; Bengio, Y.; Hinton, G. [Deep learning](https://www.nature.com/articles/nature14539). Nature, v. 521, n. 7553, p. 436–444, 2015.
8. Martinovic, A.; Knopp, J.; Riemenschneider, H.; Gool, L. V. [3D all the way: semantic segmentation of urban scenes from start to end in 3d](https://homes.esat.kuleuven.be/~konijn/publications/2015/Martinovic_3D_All_The_2015_CVPR_paper.pdf). In: CONFERENCE ON COMPUTER VISION AND PATTERN RECOGNITION. Proceedings... Boston, Massachusetts, USA: CVPR, 2015. p. 4456–4465.
9. Riemenschneider, H.; Bódis-Szomorú, A.; Weissenberg, J.; Gool, L. V. [Learning where to classify in multi-view semantic segmentation](http://www.vision.ee.ethz.ch/~rhayko/paper/eccv2014_riemenschneider_multiviewsemseg.pdf). In: EUROPEAN CONFERENCE ON COMPUTER VISION. Proceedings... Zurich, Switzerland: ECCV, 2014. p. 516–532. 

