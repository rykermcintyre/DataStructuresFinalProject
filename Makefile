CXX=		g++
CXXFLAGS=	-g -std=gnu++11
LD=			g++
LDFLAGS=	
LIBRARY=	libmap.a
LIB_SRC=	trie.cpp rbtree.cpp linkedlist.cpp 
LIB_OBJ=	$(LIB_SRC:.cpp=.o)

PROGRAMS=	testtrie testrbtree testlinkedlist hash

all: $(LIBRARY) $(PROGRAMS)

%.o: %.cpp project.h
	$(CXX) $(CXXFLAGS) -o $@ -c $<

$(LIBRARY):	$(LIB_OBJ)
	$(AR) $(ARFLAGS) $@ $(LIB_OBJ)

testtrie: testtrie.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

testrbtree: testrbtree.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

testlinkedlist: testlinkedlist.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

hash: hash.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

clean:
	rm -f $(LIBRARY) $(PROGRAMS) *.o
