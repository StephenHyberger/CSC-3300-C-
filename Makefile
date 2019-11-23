CPP_CONNECTOR_DIR = Connector\C++
CPPFLAGS = -I $(CPP_CONNECTOR_DIR)\include -L $(CPP_CONNECTOR_DIR)\lib
LDLIBS = -lmysqlcppconn8
CXXFLAGS = -std=c++11
all : objects\Driver.o
	g++ objects\Driver.o -o Driver.exe 
objects\Driver.o: sources\Driver.cpp
	g++ $(CXXFLAGS) $(CPPFLAGS) $(LDLIBS) -c sources\Driver.cpp -o objects\Driver.o  
clean :  
	del Driver.exe objects\Driver.o