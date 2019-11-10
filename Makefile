
all : objects\Driver.o
	g++ objects\Driver.o -o Driver.exe 
objects\Driver.o: sources\Driver.cpp
	g++ -c sources\Driver.cpp -o objects\Driver.o  
clean :  
	del Driver.exe objects\Driver.o