%A replacement simple and computationally efficient Gaussian Radial Basis function
%Uses: RBF Neural Networks
function a = sq_rbf(n,param)
			m = abs(n); 
			a = (m < 1) .* (1 - m.^2/2)             + ...
                  (m >=1 & m < 2)   .* ((2 - m).^2/2);
end

