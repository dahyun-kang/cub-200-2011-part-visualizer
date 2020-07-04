# CUB-200-2011 part visualizer

This repository visualizes CUB-200-2011 part keypoints (Wah et al.).

<img src = "figs/bunting.png" width="70%"></center>
<img src = "figs/warbler.png" width="70%"></center>
<img src = "figs/fulmar.png" width="70%"></center>

## Requirements
* Python
* PyTorch
* matplotlib
* PIL

## Quick startup
plot one bird: 
```
  viz.py --img_path $YOUR_PATH_FOR_CUB_ORIGIN_FOLDER/images/012.Yellow_headed_Blackbird/Yellow_Headed_Blackbird_0059_8079.jpg
```
plot all birds: 
```
  viz.py --plot_order {randomly, in_order}
```

## References
Wah, Catherine, et al. "The caltech-ucsd birds-200-2011 dataset." (2011).
