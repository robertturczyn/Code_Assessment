# Code_Assessment

This simply python script will let you grab the body of a webpage and store it in a text file called body.txt. It also will create a second file called checksum.txt that will store the checksum of body.txt inside it. 

This project was designed with python3.7 and will work best with it. 

You will need to import BeautifulSoup and Requests if you don't have them installed. 

```
pip3 install requests
pip3 install beautifulsoup4
```

To run the program simply run:
```
python3 get_body.py
```
It will ask you what website you would like to grab the body from. Make sure you enter in the entire website url. For example https://wwww.google.com

After that you will be prompt if you want the just the text of the body by selecting 1 or grabbing the entire html markup for the body of the site by selecting 2. 

Once you make your selection both text files will be created in your current working directory. 
