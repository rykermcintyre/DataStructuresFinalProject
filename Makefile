CXX=		g++
CXXFLAGS=	-g -std=gnu++11
LD=			g++
LDFLAGS=	
LIBRARY=	libmap.a
LIB_SRC=	trie.cpp rbtree.cpp linkedlist.cpp sepchain.cpp 
LIB_OBJ=	$(LIB_SRC:.cpp=.o)

PROGRAMS=	continuous testtrie testrbtree testlinkedlist hash testsepchain load load2

all: $(LIBRARY) $(PROGRAMS)

test: testtrie testrbtree testlinkedlist testsepchain
	@echo "Testing trie..."
	./testtrie > testtrie.txt
	@diff -q testtrie.txt out_testtrie.txt
	@echo "Testing rbtree..."
	./testrbtree > testrbtree.txt
	@diff -q testrbtree.txt out_testrbtree.txt
	@echo "Testing linkedlist..."
	./testlinkedlist > testlinkedlist.txt
	@diff -q testlinkedlist.txt out_testlinkedlist.txt
	@echo "Testing sepchain..."
	./testsepchain > testsepchain.txt
	@diff -q testsepchain.txt out_sepchain.txt

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

load: load.o $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

testsepchain: testsepchain.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

continuous: continuous.o project.h $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

load2: load2.o $(LIBRARY)
	$(LD) $(LDFLAGS) -o $@ $< $(LIBRARY)

clean:
	rm -f $(LIBRARY) $(PROGRAMS) *.o testlinkedlist.txt testtrie.txt testrbtree.txt testsepchain.txt

