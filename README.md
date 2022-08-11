# termchars
* build unicode width table
* present a function to query the width of unicode

# Usage

- termchars.substr(origin, begin, width, fill=True)
  + extract substring from `begin` with `width` characters (bytes)
  + if fill is False and `begin` is in the middle of a character, then adjust `begin` to the start of the character
  + if fill is True and `begin` is in the middle of a character, then a space is prefixed and adjust `begin` to the next of the character
  + if fill is False and `width` ends in the middle of a character, then ignore the last character.
  + if fill is True and `width` ends in the middle of a character, then, fill a blank instead of ignoring it.
  + if fill is True and `width` is bigger than the last of string, then, fill blanks to make wanted width.

- char_widths.json is JSON format, you can freely use it for other purpose, or other languages.

# Sample

```python
import termchars

haystack = "말할 수 없는 것에 관해서는 침묵해야 한다."
print( "({},{},True) BEG:".format(0, 1) + termchars.substr(haystack, 0, 1) + ":END" )
print( "({},{},True) BEG:".format(0, 2) + termchars.substr(haystack, 0, 2) + ":END" )
print( "({},{},True) BEG:".format(0, 3) + termchars.substr(haystack, 0, 3) + ":END" )
print( "({},{},True) BEG:".format(0, 4) + termchars.substr(haystack, 0, 4) + ":END" )
print( "({},{},True) BEG:".format(0, 5) + termchars.substr(haystack, 0, 5) + ":END" )
print( "({},{},True) BEG:".format(0, 6) + termchars.substr(haystack, 0, 6) + ":END" )
print( "({},{},True) BEG:".format(0, 7) + termchars.substr(haystack, 0, 7) + ":END" )
print( "--" )
print( "({},{},True) BEG:".format(0, 10) + termchars.substr(haystack, 0, 10) + ":END" )
print( "({},{},True) BEG:".format(1, 10) + termchars.substr(haystack, 1, 10) + ":END" )
print( "({},{},True) BEG:".format(2, 10) + termchars.substr(haystack, 2, 10) + ":END" )
print( "({},{},True) BEG:".format(3, 10) + termchars.substr(haystack, 3, 10) + ":END" )
print( "({},{},True) BEG:".format(4, 10) + termchars.substr(haystack, 4, 10) + ":END" )
print( "({},{},True) BEG:".format(5, 10) + termchars.substr(haystack, 5, 10) + ":END" )
print( "({},{},True) BEG:".format(6, 10) + termchars.substr(haystack, 6, 10) + ":END" )
print( "--" )
haystack = "あの風は誰を呼ぶのか雨の影"
print( "({},{},True) BEG:".format(12, 1) + termchars.substr(haystack, 12, 1) + ":END" )
print( "({},{},True) BEG:".format(12, 4) + termchars.substr(haystack, 12, 4) + ":END" )
print( "({},{},True) BEG:".format(12, 7) + termchars.substr(haystack, 12, 7) + ":END" )
print( "({},{},True) BEG:".format(12, 10) + termchars.substr(haystack, 12, 10) + ":END" )
print( "({},{},True) BEG:".format(12, 13) + termchars.substr(haystack, 12, 13) + ":END" )
print( "({},{},True) BEG:".format(12, 16) + termchars.substr(haystack, 12, 16) + ":END" )
print( "({},{},True) BEG:".format(12, 19) + termchars.substr(haystack, 12, 19) + ":END" )
print( "--" )
print( "({},{},False) BEG:".format(12, 1) + termchars.substr(haystack, 12, 1, False) + ":END" )
print( "({},{},False) BEG:".format(12, 4) + termchars.substr(haystack, 12, 4, False) + ":END" )
print( "({},{},False) BEG:".format(12, 7) + termchars.substr(haystack, 12, 7, False) + ":END" )
print( "({},{},False) BEG:".format(12, 10) + termchars.substr(haystack, 12, 10, False) + ":END" )
print( "({},{},False) BEG:".format(12, 13) + termchars.substr(haystack, 12, 13, False) + ":END" )
print( "({},{},False) BEG:".format(12, 16) + termchars.substr(haystack, 12, 16, False) + ":END" )
print( "({},{},False) BEG:".format(12, 19) + termchars.substr(haystack, 12, 19, False) + ":END" )
print( "--" )
```
```bash
$ python3 test.py
(0,1,True) BEG: :END
(0,2,True) BEG:말:END
(0,3,True) BEG:말 :END
(0,4,True) BEG:말할:END
(0,5,True) BEG:말할 :END
(0,6,True) BEG:말할  :END
(0,7,True) BEG:말할 수:END
--
(0,10,True) BEG:말할 수 없:END
(1,10,True) BEG: 할 수 없 :END
(2,10,True) BEG:할 수 없는:END
(3,10,True) BEG:  수 없는 :END
(4,10,True) BEG: 수 없는  :END
(5,10,True) BEG:수 없는 것:END
(6,10,True) BEG:  없는 것 :END
--
(12,1,True) BEG: :END
(12,4,True) BEG:呼ぶ:END
(12,7,True) BEG:呼ぶの :END
(12,10,True) BEG:呼ぶのか雨:END
(12,13,True) BEG:呼ぶのか雨の :END
(12,16,True) BEG:呼ぶのか雨の影  :END
(12,19,True) BEG:呼ぶのか雨の影     :END
--
(12,1,False) BEG::END
(12,4,False) BEG:呼ぶ:END
(12,7,False) BEG:呼ぶの:END
(12,10,False) BEG:呼ぶのか雨:END
(12,13,False) BEG:呼ぶのか雨の:END
(12,16,False) BEG:呼ぶのか雨の影:END
(12,19,False) BEG:呼ぶのか雨の影:END
--
```
