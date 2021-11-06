# TWO POINT SCIENCE

An attempt at applying analytical science to the game Two Point Hospital.

## BACKGROUND

[Two Point Hospital](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwig1p_w0v3zAhWObc0KHWpMAfoQFnoECAQQAQ&url=http%3A%2F%2Fwww.twopointhospital.com%2F&usg=AOvVaw3GGa9E7TMAXQYTby7TBfyd) is a humurous business simulation game focused on hospital management.  With all the DLC, there are 33 hospitals to manage each with its own unique layout, environmental considerations, and (most importantly) a unique list of ailments to diagnose and treat.

## GOAL

The goal of this project is to programmatically aid the planning of each unique hospital based on room density and patient "pathing", if "pathing" is defined as "the a->b->c->d room path each patient takes as they are diagnosed and treated."

## DETAILS

two_point_science is written in Python 3.8.10 and relies heavily on the graphviz Python library.  It was developed in Ubuntu 20.04.3 LTS.

## FEATURES

The `tps` package currently generates an undirected acyclic graph for [Grockle Bay](https://two-point-hospital.fandom.com/wiki/Grockle_Bay).

### Usage

```
git clone https://github.com/hark130/two_point_science.git
python -m tps
```

### Future Feature Table

| Feature Number | Status | Branch Name | Description |
| :------------: | :----: | :---------- | :---------- |
| 1  | ❔ | wheel | Programmatically build a wheel that can be installed |
| 2  | ❔ | cli | Create a user interface (e.g., CLI menu, config file)  |
| 3  | ❔ | color | Color code things (e.g., nodes, edges) based on what's happening (e.g., diag, treat) |
| 4  | ❔ | graph_polish | Is there a better way to align the node labels?  Reduce noisy parallel edges? |
| 5  | ❔ | names | Refactor tph_constants to use MACROS for proper names |
| 6  | ❔ | weight | Define key illneses per hospital (e.g., Grockle Bay + Cubism) |
| 7  | ❔ | suggest_rooms | Suggest number of rooms based on hospital illness list |
| 8  | ❔ | suggest_staff | Suggest staff list based on suggested room list |
| 9  | ❔ | treat_path | Plot all paths to a given treatment room |
| 10 | ❔ | ill_path | Plot all paths for a given illness |
| 11 | ❔ | diag_path | Plot all paths to and from a given diagnostic room |
|   |  |  |

### Table Legend

| Icon | Meaning |
| :--: | :------ |
| ❔ | Not yet started |
| 🚧 | In progress |
| ✔️ | Finished |

## RESOURCES

- [Draw custom node icons](https://networkx.org/documentation/latest/auto_examples/drawing/plot_custom_node_icons.html#sphx-glr-auto-examples-drawing-plot-custom-node-icons-py)
- [Two Point Hospital](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwig1p_w0v3zAhWObc0KHWpMAfoQFnoECAQQAQ&url=http%3A%2F%2Fwww.twopointhospital.com%2F&usg=AOvVaw3GGa9E7TMAXQYTby7TBfyd) official page
- [Two Point Hospital](https://en.wikipedia.org/wiki/Two_Point_Hospital) wiki
- [Two Point Hospital](https://two-point-hospital.fandom.com/wiki/Two_Point_Hospital_Wiki) primary data source
- [List of hospitals](https://two-point-hospital.fandom.com/wiki/Hospitals)
- [List of illnesses](https://gamefaqs.gamespot.com/pc/230622-two-point-hospital/faqs/76595/list-of-illnesses)
- [Treatment formula](https://www.reddit.com/r/TwoPointHospital/comments/b3x2ky/treatment_formula/)
- [Illness list with diagnosis modifiers](https://www.reddit.com/r/TwoPointHospital/comments/9husy9/full_illnesses_and_diagnosis_modifiers_finally/)
- [Graphy gallery](https://www.python-graph-gallery.com/)
- [Graphy Theory notes](https://math.stackexchange.com/questions/655589/what-is-difference-between-cycle-path-and-circuit-in-graph-theory)
- [Graphy coloring](https://en.wikipedia.org/wiki/Graph_coloring)
- [graphviz](http://graphviz.org/documentation/) (an alternative to the current underlying Python modules)

## NOTES

### TO DO: DON'T DO NOW

- [X] Add a CHANGELOG
- [ ] Consider adding edges between the first diagnostic room and treatement room (to represent skilled staff with upgraded equipment (new feature?  Hospital Age: new (full path), skilled (GP->diag1->treat))
- [X] Add file comment blocks
- [X] Run Pylint
- [X] Run Pycodestyle
- [X] Define wiki (e.g., Usage, Release Steps, Code Review)
- [ ] Find a way to deconflict "public record" and observations when it comes to the illness list for a given hospital
	- [X] Grockle Bay

### BUGS

- [X] Blighton was listed with Premature Mummification.  Loading Blighton resulted in a `NotImplementedError: Blighton has an illness, Premature Mummification, missing a treatment room.`.  Theory: The treatment room for Premature Mummification wasn't part of the room list, it wasn't validated, so it didn't load into the Illness class.  Reason: Treatment room was incorrectly configured for the given illness.
