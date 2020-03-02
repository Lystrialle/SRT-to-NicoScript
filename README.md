# SRT to NicoScript

This is a script meant to help convert standard SRT subtitle files to the NicoScript used by Nico Nico Douga for its "uploader comments", thus allowing a video uploader to effectively make captions/subtitles for their video without too much legwork.

This script is made for use with Notepad++ and its Python Scripts plugin.

1. Install [Notepad++](https://notepad-plus-plus.org/) if you haven't already.

2. Install the Notepad++ Python Script plugin.
(In Notepad++, Plugins -> Plugins Admin -> Python Script -> Install)

3. Create a new Python Script with the plugin (Plugins -> Python Script -> New Script -> name it whatever you like), copy and paste the contents of [SRT-to-NicoScript.py](../blob/master/SRT-to-NicoScript.py) in, and save.
**Alternatively**, place the [SRT-to-NicoScript.py](../blob/master/SRT-to-NicoScript.py) file into your Python Script folder, usually C:\Users\{{your name}}\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts.

4. Open your desired SRT file in Notepad++.

5. Run the script on it (Plugins -> Python Script -> Scripts -> whatever the script here is named).

6. Log into Nico Nico Douga and go to the video you want to insert the subtitles into.

7. At the top toolbar, hit **編集**, and then **投稿者コメントを編集**.

8. On the window that appears next to the video, hit **エディター表示**.

9. Copy and paste the contents of the script-modified SRT file from Notepad++ into the window (overwrite the brackets that are in there).

10. Click **リスト反映** to reflect changes, then **編集を終了**.

11. Done!

## Notes

* This script uses the HTML5 version of NicoScript, and won't work with Flash.

* The script is configured with the assumption that it'll be used for subtitles/captions, and so it sets all the comments to default color (white), centered, and small at the bottom of the frame to not be intrusive (much like real subtitles). If you want to do anything fancier or different, refer to the [official documentation on Nico Nico Douga](https://qa.nicovideo.jp/faq/show/7386?category_id=413) (you can use Notepad++'s search-and-replace functions to customize it to your liking).

* Where a block of text in the SRT had multiple lines, the script will split these into multiple comments and have them display simultaneously on the screen (they're also submitted as comments in reverse order, so that they'll appear in the right order vertically when they actually show up as comments).

* Technically speaking, this script breaks if your video is longer than 99 hours, 59 minutes, 59 seconds, and 999 milliseconds, but honestly, if your video is that long, I think you might have other things you need to be worrying about.

* Because SRT is made for milliseconds and NicoScript takes hundredths of seconds, I had the script round down to the nearest hundredth, which means that (unlike with real subtitles) things will vanish a barely-noticeable amount of time earlier than usual.
