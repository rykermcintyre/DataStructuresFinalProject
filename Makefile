CXX=		g++
CXXFLAGS=	-g -std=gnu++11
LD=			g++
LDFLAGS=	

all: testtrie

%.o: %.cpp project.h
	$(CXX) $(CXXFLAGS) -o $@ -c $<

testtrie: testtrie.o trie.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f testtrie
