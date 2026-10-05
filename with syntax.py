with open("demo.txt","r")as g:        #from {open("demo.txt","r")} we call it as a stream of g.
                                    #as:-  refers to alias which is used to refer the stream of g.
    print(g.read())


## WE DONT NEED TO CLOSE THE FILE WHEN WE USE WITH OPEN() AS IT AUTOMATICALLY CLOSES THE FILE AFTER EXECUTION OF THE BLOCK OF CODE.



##writing to a file using with open() method:-

with open("demo.txt", "w") as f:
  f.write("new data entered")
  