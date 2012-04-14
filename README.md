Blender - Social Location
=========================

This is a very simple script, intended for use on text media (such as IRC or
forums) when discussing a `.blend`.

The idea is that you and a buddy can be looking at the same `.blend` file, and
you can go to the `'n' Properties Panel > 3D Cursor` and hit a single button
for `Copy`, then paste the "`x, y, z`" string to your friend, who can then copy
it and click the corresponding `Paste` button inside his Blender.

Through this relatively painless set of steps, you precisely pointed out a
spot that can be used for the remainder of the communication. This is most
clearly useful when discussing the details of topology. You can say "The Edge
Loop that is formed from `Alt+RMB`ing on the point 1.234, 5.678, 9.1011".

A handy tool to use with this is `Ctrl+Numpad '.'`, to center the 3D Viewport
on the 3D Cursor -- sometimes followed-on with some zooming.

With a little innovation, you could even make that location mean something
more -- for example, you could `Shift+a > Mesh > Plane` then `Tab` into Edit
Mode, and do `Alt+m,a` to merge the verts at the center, thus leaving you with
exactly one vert at that exact location.

You could even do an entire model this way, through placing points, placing
the cursor at a different point, then `f`illing an edge/face,  if you had two
people whose patience bordered on the infinite. =)

Example
-------

0. Copy this into clipboard: `1.1, 0.43, 0.315`
0. Start Blender with a Default Scene.
0. Delete the Default Cube (but don't enjoy it -- ever).
0. `Shift+a > Mesh > Monkey`
0. `Tab` into Edit Mode.
0. Click `'n' Panel > 3D Cursor > Paste`
0. Maybe hit `Ctrl+Numpad '.'`
0. How many verts does that face have?
0. Ha! They should have used [MeshLint](https://github.com/ryanjosephking/meshlint)!

Independence
------------

There is nothing special about the values going into / out of the clipboard.
You could manually make them (so even if only one user is running the `Social
Location` Addon, all it means is the other has to manually paste the
components rather than doing them in one shot). Also, this means that you can
edit the string as you wish (see: Precision, below, for an example of
circumstances where you may want to manually affect the values for
aesthetics).

Getting
-------

Best way is to:

    git clone git@github.com:ryanjosephking/soc-loc.git

That way, you can `git pull` later on and it will automatically refresh to the
latest (theoretically-)good version.

But I realize that not everyone has `git` or an operating system capable of
symlinking.

So, for those that can't: You can simply download the
[soc-loc.py](https://raw.github.com/ryanjosephking/soc-loc/master/soc-loc.py)
script directly. (And re-visit that URL for the newest version, later on.)

Installing
----------

The super-awesome way is to directly symlink `soc-loc.py` into your [Blender
Addons
Dir](http://wiki.blender.org/index.php/Doc:2.6/Manual/Introduction/Installing_Blender/DirectoryLayout).
The advantage is that the previous section's `git pull` will download the
newest version automatically. But not everyone can be expected to be
superawesome all the time, so continue on:

![Installing Addon](soc-loc/raw/master/img/install-addon.png "`Install Addon...` screen.")

Hit `Ctrl+Alt+u` to load up the User Preferences (I always use the keystroke
for this because of the occasional time where you miss, using the `File` menu,
and click `Save User Settings`. Click the `Install Addon...` button at the
bottom, then navigate to your `soc-loc.py` script.

![The Enable Checkbox](soc-loc/raw/master/img/enable-checkbox.png "The Enable checkbox.")

Next, and this is a tricky bit, if you're not used to installing Addons: you
have to follow up by checking this little box on the right of the Addon entry
in the list. If, for some reason, you have a hard time finding it, you can
search for `Social Location` or click on the `Mesh` button on the left.
Hopefully, though, it comes right up when you do `Install Addon...`.

If you want to keep `Social Location` available (and who wouldn't?), follow
the above steps on a fresh `.blend` (one you `Ctrl+n`d), then hit `Ctrl+u` at
this point. The next time you run Blender you won't have to repeat the above.

![Where is it? -> 'n' Properties Panel > 3D
Cursor](soc-loc/raw/master/img/where-is-it.png "'n' Properties Panel > 3D
Cursor")

When installed, it will add to the existing `'n' Properties Panel > 3D Cursor`
Subpanel. All it is: a row with a 3D Cursor icon and Copy + Paste buttons.

Precision
---------

If you are used to floating-point numbers and CPUs, you'll know that 1.0
generally isn't 1.0, but 1.000000000034, or something. In this case, it is no
different. That means that sometimes you will place your cursor precisely at,
way, `2.0, 3.0, 0.0`, but it will paste to your buddy as something close to
that. We thought about (and are still thinking about) the idea of rounding it,
but we didn't want to lose accuracy by rounding up or down, even if it would
help "Snap" the cursor to prettier-seeming coordinates.

Basically, you can treat the components as a black box, and not worry about
them - when you go to point out things in the 3D world, it will get you as
close as we know how.

If you have a strong case for or against rounding, please let us know.

Going Further
-------------

Bug reports / feature requests / brainstorm lightning bolts / broad criticisms
are always welcome!

<rking@panoptic.com>
