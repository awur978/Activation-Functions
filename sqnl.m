function a = sqnl(n,param)

% Copyright 2012 The MathWorks, Inc.

a=zeros(size(n));

idx = find(n > 2);
n(idx) = 2;

idx = find(n < -2);
n(idx) = -2;


idx = find(n >= 0);
a(idx) = n(idx) - n(idx).^2/4;

idx = find(n < 0);
a(idx) = n(idx) + n(idx).^2/4;
