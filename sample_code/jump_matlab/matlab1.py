import matlab.engine
eng = matlab.engine.start_matlab()
for i in range(10):
    eng.triarea(nargout=0)