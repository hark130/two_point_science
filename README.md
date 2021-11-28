# TWO POINT SCIENCE

An attempt at applying analytical science to the game Two Point Hospital.

## BACKGROUND

[Two Point Hospital](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwig1p_w0v3zAhWObc0KHWpMAfoQFnoECAQQAQ&url=http%3A%2F%2Fwww.twopointhospital.com%2F&usg=AOvVaw3GGa9E7TMAXQYTby7TBfyd) is a humurous business simulation game focused on hospital management.  With all the DLC, there are 33 hospitals to manage each with its own unique layout, environmental considerations, and (most importantly) a unique list of ailments to diagnose and treat.

## GOAL

The goal of this project is to programmatically aid the planning of each unique hospital based on room density and patient "pathing", if "pathing" is defined as "the a->b->c->d room path each patient takes as they are diagnosed and treated".

## DETAILS

two_point_science is written in Python 3.8.10 and relies heavily on the graphviz Python library.  It was developed in Ubuntu 20.04.3 LTS.

## FEATURES

The `tps` package currently implements the following hospitals:

- Blighton
- Clockwise-above-Thyme
- Croquembouche
- Grockle Bay
- Mitton University
- Pelican Wharf
- Rotting Hill
- Smogley
- Sweaty Palms

### Usage

See: [Usage](https://github.com/hark130/two_point_science/wiki/usage) wiki page

### Future Feature Table

| Feature Number | Status | Branch Name | Description |
| :------------: | :----: | :---------- | :---------- |
| 1  | ❔ | wheel | Programmatically build a wheel that can be installed |
| 2  | ✔️ | menu | Create a user interface (e.g., CLI menu, config file) |
| 3  | ❔ | color | Color code things (e.g., nodes, edges) based on what's happening (e.g., diag, treat) |
| 4  | ❔ | graph_polish | Is there a better way to align the node labels?  Reduce noisy parallel edges? |
| 5  | ❔ | names | Refactor tph_constants to use MACROS for proper names |
| 6  | ❔ | weight | Define key illneses per hospital (e.g., Grockle Bay + Cubism) and add graph callout (e.g., bold?) |
| 7  | ❔ | suggest_rooms | Suggest number of rooms based on hospital illness list |
| 8  | ❔ | suggest_staff | Suggest staff list based on suggested room list |
| 9  | ✔️ | room_path | Plot all edges for a given room |
| 10 | 🚧 | ill_path | Plot all paths for a given illness |
| 11 | ❔ | change_default | Add a "change defaults" entry to the main menu |
| 12 | ✔️ | cli | Add support for CLI arguments (e.g., --distinct-rooms) |
| 13 | ✔️ | edges | CLI menu option to display sorted and/or filtered list of rooms/purpose/number of edges |
| 14 | ❔ | shell | CLI argument to change the default graph type (e.g., shell could be of use?) |
| 15 | ❔ | dyn_menu | Dynamic menu items (e.g., "Choose a hospital" becomes "Change hospitals (Currently: blahblahblah)") |
| 16 | ❔ | default | Add a "default choice" optional kwarg to the menu module functions |
| 17 | ❔ | menu_banner | Add a fancy banner about menu headers |
| 18 | ❔ | table_banner | Add a fancy banner about table headers |
| 19 | ❔ | sep_suffix | There's a dangerous amount of hard-coded suffix strings.  SPOT it! |
| 20 | ✔️ | graph_dir | CLI argument to specify a directory to save graph filenames |
| 21 | ✔️ | danger | Add menu functionality to rank the treat rooms by (avg. and worst) danger (e.g., illness difficulty * rate of decline) |
|   |  |  |  |

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
- [ ] Consider adding edges between the first diagnostic room and treatement room (to represent skilled staff with upgraded equipment (new feature?  Hospital Age: new (full path), skilled (GP->diag1->treat))  EDIT: Maybe this is a CLI argument (e.g., --age={amateur,skilled})
- [X] Add file comment blocks
- [X] Run Pylint
- [X] Run Pycodestyle
- [X] Define wiki (e.g., Usage, Release Steps, Code Review)
- [ ] Find a way to deconflict "public record" and observations when it comes to the illness list for a given hospital
	- [X] Grockle Bay
	- [X] Mitton University
- [ ] Is exception.args[0] deprecated?  Yes or no, should I be using exception.msg instead?  (see: misc.print_exception()
- [ ] Investigate mypy: replace isinstance() calls?, verify safe variable usage?
- [ ] Extricate *_menu() functions into a separate tps.menus.py (or the menu.py) module
- [ ] Extricate print_*_table() functions into a separate tps.tables.py module (or make a class?)

### BUGS

- [X] Blighton was listed with Premature Mummification.  Loading Blighton resulted in a `NotImplementedError: Blighton has an illness, Premature Mummification, missing a treatment room.`.  Theory: The treatment room for Premature Mummification wasn't part of the room list, it wasn't validated, so it didn't load into the Illness class.  Reason: Treatment room was incorrectly configured for the given illness.
- [ ] Add quit feature to menu functionality.  Take care to avoid a dict.keys() collision.
- [X] distinct-rooms CLI argument does nothing for printing room edge list.  It has to do with room edges are detected in the graph_obj.body.
- [X] CLI menu vertical whitespacing could use some polish
- [ ] Ward (treat) appears in the "room connection" table for Blighton (-d) but is not listed as a treatment on the graph (because there is no illness treated in a Ward at this hospital)
- [ ] Ward connection counts are being shared by both (treat) and (diag) in the "room connection" table for Pelican Wharf (-d) even though the main graph doesn't support those numbers visually
- [X] "PELICAN WHARFROOM LIST"
- [ ] Consider shortening dgraph.create_graph() protoptype with a Class or NameTuple (then remove the pylint disable)
