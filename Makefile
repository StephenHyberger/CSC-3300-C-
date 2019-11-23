CPP_CONNECTOR_DIR = "C:\Program Files\MySQL\Connector C++ 8.0
CPPFLAGS = -I $(CPP_CONNECTOR_DIR)\include" -L $(CPP_CONNECTOR_DIR)\lib64"
LDLIBS = -lmysqlcppconn8
CXXFLAGS = -std=c++11
all : objects\Driver.o
	g++ objects\Driver.o -o Driver.exe 
objects\Driver.o: sources\Driver.cpp
	g++ $(CXXFLAGS) $(CPPFLAGS) $(LDLIBS) -c sources\Driver.cpp -o objects\Driver.o  
clean :  
	del *.exe objects\*.o
