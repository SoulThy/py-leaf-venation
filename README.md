A Python implementation of the leaf venation algorithm.

## Inspiration
This project was inspired by Tsoding, who implemented a similar simulation in C (check out his version [here](https://github.com/tsoding/leaf-venation)). 
I decided to build this in Python just for fun, without looking at his implementation. I am fully aware that my implementation is highly inefficient in several areas, but it serves its purpose as an exploratory project.

## Algorithm Reference
The algorithm follows the description in the paper:
[Modeling and Visualization of Leaf Venation Patterns](https://dl.acm.org/doi/10.1145/1186822.1073251) (Section "3.4 Example").
A local copy of the PDF is available in `docs/modeling_and_visualization_of_leaf_venation_patterns.pdf`.

You can also find a reference screenshot from section 3.4 in `docs/illustration_of_the_algorithm.png`.

![Algorithm Illustration](docs/illustration_of_the_algorithm.png)

## Recordings / Demonstrations

Here are some visual recordings of the simulation running under different parameters:

### Top-Left Starting Position
- [Auxin Collision Radius 5x Density](docs/recordings/top_left_CR_5x.mp4)
- [Auxin Collision Radius 20x Density](docs/recordings/top_left_CR_20x.mp4)

### Center Starting Position
- [Auxin Collision Radius 5x Density](docs/recordings/center_CR_5x.mp4)
- [Auxin Collision Radius 20x Density](docs/recordings/center_CR_20x.mp4)

## Prerequisites & Usage

Ensure you have [uv](https://github.com/astral-sh/uv) installed. You can run the project directly with:

```bash
uv run main.py
```

You can stop the execution early by using '**q**'.

By default the simulations runs automatically, in case `AUTO_MODE` is set to `False` then *SPACEBAR* can be used to step forward the simulation.
```py
AUTO_MODE = True
FPS = 30 
```

