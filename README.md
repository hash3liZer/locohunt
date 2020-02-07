<h1 align="center"> 
    <img src="https://user-images.githubusercontent.com/29171692/74031823-57041080-49d4-11ea-9900-37e1bfd21ee8.png" alt="locohunt" /> <br>    
    LOCOHUNT
</h1>
<h4 align="center">Search for Secrets and Other Confidential Information Through Directories and Files Based on Regex and Search Strings. </h4>
<p align="center">
    <a href="https://www.gnu.org/licenses/gpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="lisence" /></a>
</p>

## Description
This tool is inspired from <a href="https://github.com/dxa4481/truffleHog">truffleHog</a> which was built to explore and search for api keys and other confidential information through a github repo commit repository. This tool is built to do the same but on directories by using the Regular Expressions. 

## Manual
```
    Args              Description                  Default
    -h, --help        Print Manual                  False
    -t, --target      Target File or Directory
                      for Searching and 
                      Scanning                      None
    -r, --regex       Single Regex to Search
                      against the files.            None
    -f, --regex-json  File Containing multiple
                      Regular Expressions in JSON
                      Format.                       Inner
    -d, --depth       Depth of Directories          All
```

## Regex
To Use Your own Regex file, you need to give in JSON form. An example is given <a href="https://github.com/dxa4481/truffleHogRegexes/blob/master/truffleHogRegexes/regexes.json">here</a>

## Credits
Author: <a href="https://twitter.com/hash3liZer">@hash3liZer</a>
