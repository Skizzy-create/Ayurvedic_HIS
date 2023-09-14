<div class="container">
<h1>Optimizers in Machine Learning</h1>

<p>Optimizers are algorithms or methods used to adjust the parameters of your neural network model to reduce the errors or losses of predictions. There are several types of optimizers, including Gradient Descent (GD), Momentum, RMSprop, Adam, and AdamW.</p>

<h2>Mean Squared Error (MSE)</h2>

<p>Mean Squared Error (MSE) is a common loss function used in machine learning that measures the average squared difference between the estimated values and the actual value. It's defined as:</p>

<div class="formula">
<b>MSE = 1/n Σ(actual value - predicted value)²</b>
</div>

<p>The smaller the MSE, the closer we are to finding the line of best fit.</p>

<h2>Gradient Descent (GD)</h2>

<p>Gradient Descent is an optimization algorithm that's used when training a machine learning model. It's based on iteratively adjusting the parameters of the model, in order to minimize the given function to its local minimum.</p>

<div class="formula">
<b>θ = θ - η * ∇J(θ)</b>
</div>

<p>where:</p>
<ul>
<li>θ is the parameter (a vector).</li>
<li>η is the learning rate (a scalar).</li>
<li>∇J(θ) is the gradient of the loss function.</li>
</ul>

<h2>Momentum</h2>

<p>Momentum is a method that helps accelerate gradients vectors in the right directions, thus leading to faster converging. It is inspired by the physical concept of momentum, as its name suggests.</p>

<div class="formula">
<b>v = γv + η∇J(θ)</b>
<b>θ = θ - v</b>
</div>

<p>where:</p>
<ul>
<li>v is the velocity (a vector).</li>
<li>γ is the momentum (a scalar).</li>
</ul>

<h2>RMSprop</h2>

<p>RMSprop (Root Mean Square Propagation) is an optimizer that utilizes the magnitude of the recent gradient descents to normalize the gradient. It's mainly used to resolve the diminishing learning rates issue of AdaGrad.</p>

<div class="formula">
<b>s = βs + (1 - β)(∇J(θ))^2</b>
<b>θ = θ - η*∇J(θ)/sqrt(s + ε)</b>
</div>

<p>where:</p>
<ul>
<li>s is the accumulated square gradient vector.</li>
<li>β is the forgetting factor.</li>
<li>ε is a small number to avoid division by zero.</li>
</ul>

<h2>Adam</h2>

<p>Adam (Adaptive Moment Estimation) is an optimizer that computes adaptive learning rates for each parameter. It's a combination of RMSprop and Momentum.</p>

<div class="formula">
<b>m = β1m + (1-β1)∇J(θ)</b>
<b>s = β2s + (1-β2)(∇J(θ))^2</b>
<b>θ = θ - η*m/(sqrt(s) + ε)</b>
</div>

<p>where:</p>
<ul>
<li>m is the first moment vector (the mean).</li>
<li>s is the second moment vector (the uncentered variance).</li>
</ul>

<h2>AdamW</h2>

<p>AdamW is a variant of Adam that decouples the weight decay from the optimization steps. This means it corrects the weight decay method, leading to better performance and training stability.</p>

<div class="formula">
<b>θ = (1 - λ*η) * θ</b>
<b>m = β1*m + (1-β1)*∇J(θ)</b>
<b>s = β2*s + (1-β2)*(∇J(θ))^2</b>
<b>θ = θ - η*m/(sqrt(s) + ε)</b>
</div>

<p>where:</p>
<ul>
<li>λ is the weight decay.</li>
</ul>
</div>