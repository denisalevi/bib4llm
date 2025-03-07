# Citation Key: Chaudhari - 2018 - Stochastic Gradient Descent Performs Variational Inference, Converges to Limit Cycles for Deep Netwo 1

---

# Stochastic gradient descent performs variational inference, converges to limit cycles for deep networks

### Pratik Chaudhari and Stefano Soatto

Computer Science, University of California, Los Angeles
Email: pratikac@ucla.edu, soatto@ucla.edu


**_Abstract— Stochastic gradient descent (SGD) is widely believed_**
**to perform implicit regularization when used to train deep neural**
**networks, but the precise manner in which this occurs has thus**
**far been elusive. We prove that SGD minimizes an average**
**potential over the posterior distribution of weights along with**
**an entropic regularization term. This potential is however not**
**the original loss function in general. So SGD does perform**
**variational inference, but for a different loss than the one used**
**to compute the gradients. Even more surprisingly, SGD does**
**not even converge in the classical sense: we show that the most**
**likely trajectories of SGD for deep networks do not behave like**
**Brownian motion around critical points. Instead, they resemble**
**closed loops with deterministic components. We prove that such**
**“out-of-equilibrium” behavior is a consequence of highly non-**
**isotropic gradient noise in SGD; the covariance matrix of mini-**
**batch gradients for deep networks has a rank as small as 1% of**
**its dimension. We provide extensive empirical validation of these**
**claims.**
**This article summarizes the findings in [1]. See the longer**
**version for background, detailed results and proofs.**

I. INTRODUCTION

Our first result is to show precisely in what sense stochastic
gradient descent (SGD) implicitly performs variational inference, as is often claimed informally in the literature. For a loss
function f (x) with weights x ∈ R[d], if ρ [ss] is the steady-state
distribution over the weights estimated by SGD,

� �
_ρ_ [ss] = arg min E x∼ρ Φ(x) _−_ _[η]_
_ρ_ 2b _[H][(][ρ][)][;]_

where H(ρ) is the entropy of the distribution ρ and η and b
are the learning rate and batch-size, respectively. The potential
Φ(x), which we characterize explicitly, is related but not
necessarily equal to f (x). It is only a function of the architecture
and the dataset. This implies that SGD implicitly performs
variational inference with a uniform prior, albeit of a different
loss than the one used to compute back-propagation gradients.
We next prove that the implicit potential Φ(x) is equal to
our chosen loss f (x) if and only if the noise in mini-batch
gradients is isotropic. This condition, however, is not satisfied
for deep networks. Empirically, we find gradient noise to be
highly non-isotropic with the rank of its covariance matrix
being about 1% of its dimension. Thus, SGD on deep networks
implicitly discovers locations where ∇Φ(x) = 0, these are not
the locations where ∇ _f_ (x) = 0. This is our second main result:
the most likely locations of SGD are not the local minima, nor
the saddle points, of the original loss. The deviation of these
critical points, which we compute explicitly scales linearly
with η/b and is typically large in practice.


When mini-batch noise is non-isotropic, SGD does not even
converge in the classical sense. We prove that, instead of
undergoing Brownian motion in the vicinity of a critical point,
trajectories have a deterministic component that causes SGD
to traverse closed loops in the weight space. We detect such
loops using a Fourier analysis of SGD trajectories. We also
show through an example that SGD with non-isotropic noise
can even converge to stable limit cycles around saddle points.

II. BACKGROUND ON CONTINUOUS-TIME SGD

Stochastic gradient descent performs the following updates
while training a network xk+1 = xk _η ∇_ _fb(xk) where η is_
_−_
the learning rate and ∇ _fb(xk) is the average gradient over a_
mini-batch b,

∇ _fb(x) =_ [1] ∇ _fk(x)._ (1)

_b_ _k[∑]∈b_

We overload notation b for both the set of examples in a minibatch and its size. We assume that weights belong to a compact
subset Ω ⊂ R[d], to ensure appropriate boundary conditions for
the evolution of steady-state densities in SGD, although all
our results hold without this assumption if the loss grows
unbounded as _x_ ∞, for instance, with weight decay as a
_∥_ _∥→_
regularizer.

**Definition 1 (Diffusion matrix D(x)). If a mini-batch is**
sampled with replacement, we show in Appendix A.1 that
the variance of mini-batch gradients is var (∇ _fb(x)) =_ _[D][(]b[x][)]_

where


Note that D(x) is independent of the learning rate η and the
batch-size b. It only depends on the weights x, architecture and
loss defined by f (x), and the dataset. We will often discuss
two cases: isotropic diffusion when D(x) is a scalar multiple
of identity, independent of x, and non-isotropic diffusion, when
_D(x) is a general function of the weights x._

We now construct a stochastic differential equation (SDE)
for the discrete-time SGD updates.

**Lemma 2 (Continuous-time SGD). The continuous-time limit**
_of SGD is given by_

�
_dx(t) = −∇_ _f_ (x) dt + 2β _[−][1]D(x) dW_ (t); (3)


_N_ �
## ∑ ∇ fk(x) ∇ fk(x)[⊤]
_k=1_


_D(x) =_


�
1
_N_


_−_ ∇ _f_ (x) ∇ _f_ (x)[⊤] _⪰_ 0. (2)


-----

_where W_ (t) is Brownian motion and β is the inverse tem_perature defined as β_ _[−][1]_ = 2[η]b[. The steady-state distribution]

_of the weights ρ(z,t) ∝_ P�x(t) = z�, evolves according to the
_Fokker-Planck equation [2, Ito form]:_

_∂ρ_ �∇ _f_ (x) ρ + _β_ _[−][1]_ ∇ _·_ �D(x) ρ�[�] (FP)

_∂t_ [=][ ∇] _[·]_

_where the notation ∇_ _v denotes the divergence ∇_ _v =_

_·_ _·_
∑i ∂xi vi(x) for any vector v(x) ∈ R[d]; the divergence operator
_is applied column-wise to matrices such as D(x)._

We refer to [3, Thm. 1] for the proof of the convergence
of discrete SGD to (3). Note that β _[−][1]_ completely captures
the magnitude of noise in SGD that depends only upon the
learning rate η and the mini-batch size b.

**Assumption 3 (Steady-state distribution exists and is**
**unique). We assume that the steady-state distribution of the**
Fokker-Planck equation (FP) exists and is unique, this is
denoted by ρ [ss](x) and satisfies,

0 = _[∂ρ]_ [ss] = ∇ _·_ �∇ _f_ (x) ρ [ss] + _β_ _[−][1]_ ∇ _·_ �D(x) ρ [ss][��]. (4)

_∂t_

III. SGD PERFORMS VARIATIONAL INFERENCE
Let us first implicitly define a potential Φ(x) using the
steady-state distribution ρ [ss]:

Φ(x) = −β _[−][1]_ log _ρ_ [ss](x), (5)

up to a constant. The potential Φ(x) depends only on the fullgradient and the diffusion matrix; see Appendix C for a proof.
It will be made explicit in Section V. We express ρ [ss] in terms
of the potential using a normalizing constant Z(β ) as

1
_ρ_ [ss](x) = (6)
_Z(β_ ) _[e][−][β]_ [Φ][(][x][)]

which is also the steady-state solution of

�
_dx = β_ _[−][1]_ ∇ _·_ _D(x) dt −_ _D(x) ∇Φ(x) dt +_ 2β _[−][1]D(x) dW_ (t)

(7)
as can be verified by direct substitution in (FP).
The above observation is very useful because it suggests that,
if ∇ _f_ (x) can be written in terms of the diffusion matrix and a
gradient term ∇Φ(x), the steady-state distribution of this SDE
is easily obtained. We exploit this observation to rewrite ∇ _f_ (x)
in terms a term D ∇Φ that gives rise to the above steady-state,
the spatial derivative of the diffusion matrix, and the remainder:

_j(x) = −∇_ _f_ (x)+ _D(x) ∇Φ(x)_ _−_ _β_ _[−][1]∇_ _·_ _D(x),_ (8)

interpreted as the part of ∇ _f_ (x) that cannot be written as
_D Φ[′](x) for some Φ[′]. We now make an important assumption_
on j(x) which has its origins in thermodynamics.

**Assumption 4 (Force j(x) is conservative). We assume that**

∇ _j(x) = 0._ (9)

_·_

The Fokker-Planck equation (FP) typically models a physical
system which exchanges energy with an external environment [4, 5]. In our case, this physical system is the gradient


dynamics ∇ (∇ _f ρ) while the interaction with the environment_

_·_
is through the term involving temperature: β _[−][1]∇_ _·_ (∇ _·_ (Dρ)).
The second law of thermodynamics states that the entropy of
a system can never decrease; in Appendix B we show how the
above assumption is sufficient to satisfy the second law. We
also discuss some properties of j(x) in Appendix C that are a
consequence of this. The most important is that j(x) is always
orthogonal to ∇ρ [ss]. We illustrate the effects of this assumption
in Example 19.

This leads us to the main result of this section.

**Theorem 5 (SGD performs variational inference). The**
_functional_

_F(ρ) = β_ _[−][1]_ KL�ρ || ρ [ss][�] (10)

_decreases monotonically along the trajectories of the Fokker-_
_Planck equation (FP) and converges to its minimum, which_
_is zero, at steady-state. Moreover, we also have an energetic-_
_entropic split_

� �
_F(ρ) = E x∈ρ_ Φ(x) _−_ _β_ _[−][1]H(ρ)+_ constant. (11)

Theorem 5 shows that SGD implicitly minimizes a combination of two terms: an “energetic” term, and an “entropic” term.
The first is the average potential over a distribution ρ. The
steady-state of SGD in (6) is such that it places most of its
probability mass in regions of the parameter space with small
values of Φ. The second shows that SGD has an implicit bias
towards solutions that maximize the entropy of ρ.
Note that the energetic term in (11) has potential Φ(x),
instead of f (x). This is an important fact and the crux of this
paper.

**Lemma 6 (Potential equals original loss iff isotropic diffu-**
**sion). If the diffusion matrix D(x) is isotropic, i.e., a constant**
_multiple of the identity, the implicit potential is the original_
_loss itself_

_D(x) = c Id×d_ _⇔_ Φ(x) = f (x). (12)

The definition in (8) shows that j = 0 when D(x) is non_̸_
isotropic. This results in a deterministic component in the SGD
dynamics which does not affect the functional F(ρ), hence
_j(x) is called a “conservative force”._

**Lemma 7 (Most likely trajectories of SGD are limit cycles).**
_The force j(x) does not decrease F(ρ) in (11) and introduces_
_a deterministic component in SGD given by_

_x˙ = j(x)._ (13)

_The condition ∇_ _j(x) = 0 in Assumption 4 implies that most_

_·_
_likely trajectories of SGD traverse closed trajectories in weight_
_space._

_A. Wasserstein gradient flow_

Theorem 5 applies for a general D(x) and it is equivalent to
the celebrated JKO functional [6] in optimal transportation [7,
8] if the diffusion matrix is isotropic.


-----

**Corollary 8 (Wasserstein gradient flow for isotropic noise).**
_If D(x) = I, trajectories of the Fokker-Planck equation (FP)_
_are gradient flow in the Wasserstein metric of the functional_

� �
_F(ρ) = E x∼ρ_ _f_ (x) _−_ _β_ _[−][1]H(ρ)._ (JKO)

Observe that the energetic term contains f (x) in Corollary 8.
The proof follows from Theorem 5 and Lemma 6, see [9] for a
rigorous treatment of Wasserstein metrics. The JKO functional
above has had an enormous impact in optimal transport because
results like Theorem 5 and Corollary 8 provide a way to modify
the functional F(ρ) in an interpretable fashion. Modifying the
Fokker-Planck equation or the SGD updates directly to enforce
regularization properties on the solutions ρ [ss] is much harder.

_B. Connection to Bayesian inference_

Note the absence of any prior in (11). On the other hand,
the evidence lower bound [10] for the dataset Ξ is,

_−_ log p(Ξ) ≤ E x∼q� _f_ (x)� + KL�q(x _|_ Ξ) || p(x _|_ Ξ)�,

_≤_ E x∼q� _f_ (x)� _−_ _H(q)+_ _H(q, p);_
(ELBO)
where H(q, p) is the cross-entropy of the estimated steadystate and the variational prior. The implicit loss function of
SGD in (11) therefore corresponds to a uniform prior p(x Ξ).
_|_
In other words, we have shown that SGD itself performs
variational optimization with a uniform prior. Note that this
prior is well-defined by our hypothesis of x Ω for some
_∈_
compact Ω.
It is important to note that SGD implicitly minimizes a
potential Φ(x) instead of the original loss f (x) in ELBO. We
prove in Section V that this potential is quite different from
_f_ (x) if the diffusion matrix D is non-isotropic, in particular,
with respect to its critical points.

**Remark 9 (SGD has an information bottleneck). The**
functional (11) is equivalent to the information bottleneck
principle in representation learning [11]. Minimizing this
functional, explicitly, has been shown to lead to invariant
representations [12]. Theorem 5 shows that SGD implicitly
contains this bottleneck and therefore begets these properties,
naturally.

**Remark 10 (ELBO prior conflicts with SGD). Working**
with ELBO in practice involves one or multiple steps of
SGD to minimize the energetic term along with an estimate
of the KL-divergence term, often using a factored Gaussian
prior [10, 13]. As Theorem 5 shows, such an approach also
enforces a uniform prior whose strength is determined by
_β_ _[−][1]_ and conflicts with the externally imposed Gaussian prior.
This conflict—which fundamentally arises from using SGD
to minimize the energetic term—has resulted in researchers
artificially modulating the strength of the KL-divergence term
using a scalar pre-factor [14].

_C. Practical implications_

We will show in Section V that the potential Φ(x) does not
depend on the optimization process, it is only a function of


the dataset and the architecture. The effect of two important
parameters, the learning rate η and the mini-batch size b
therefore completely determines the strength of the entropic
regularization term. If β _[−][1]_ _→_ 0, the implicit regularization of
SGD goes to zero. This implies that

_β_ _[−][1]_ = _[η]_

2b [should not be small]

is a good tenet for regularization of SGD.

**Remark 11 (Learning rate should scale linearly with batch–**
**size to generalize well). In order to maintain the entropic**
regularization, the learning rate η needs to scale linearly with
the batch-size b. This prediction, based on Theorem 5, fits
very well with empirical evidence wherein one obtains good
generalization performance only with small mini-batches in
deep networks [15], or via such linear scaling [16].

**Remark 12 (Sampling with replacement is better than**
**without replacement). The diffusion matrix for the case**
when mini-batches are sampled with replacement is very close
to (2), see Appendix A.2. However, the corresponding inverse
temperature is


�
should not be small.


_β_ _[′−][1]_ = _[η]_

2b


�
1
_−_ _[b]_

_N_


The extra factor of �1 _−_ _N[b]_ � reduces the entropic regularization

in (11), as b → _N, the inverse temperature β_ _[′]_ _→_ ∞. As a
consequence, for the same learning rate η and batch-size
_b, Theorem 5 predicts that sampling with replacement has_
better regularization than sampling without replacement. This
effect is particularly pronounced at large batch-sizes.

IV. EMPIRICAL CHARACTERIZATION OF SGD DYNAMICS

Section IV-A shows that the diffusion matrix D(x) for
modern deep networks is highly non-isotropic with a very low
rank. We also analyze trajectories of SGD and detect periodic
components using a frequency analysis in Section IV-B; this
validates the prediction of Lemma 7.
We consider the following three networks on the MNIST [17]
and the CIFAR-10 and CIFAR-100 datasets [18].
(i) small-lenet: a smaller version of LeNet [17] on MNIST
with batch-normalization and dropout (0.1) after both convolutional layers of 8 and 16 output channels, respectively.
The fully-connected layer has 128 hidden units. This
network has 13, 338 weights and reaches about 0.75%
training and validation error.
(ii) small-fc: a fully-connected network with two-layers,
batch-normalization and rectified linear units that takes
7 7 down-sampled images of MNIST as input and has 64
_×_
hidden units. Experiments in Section IV-B use a smaller
version of this network with 16 hidden units and 5 output
classes (30, 000 input images); this is called tiny-fc.
(iii) small-allcnn: this a smaller version of the fullyconvolutional network for CIFAR-10 and CIFAR-100
introduced by [19] with batch-normalization and 12, 24
output channels in the first and second block respectively.


-----

It has 26, 982 weights and reaches about 11% and 17%
training and validation errors, respectively.
We train the above networks with SGD with appropriate
learning rate annealing and Nesterov’s momentum set to 0.9.
We do not use any data-augmentation and pre-process data
using global contrast normalization with ZCA for CIFAR-10
and CIFAR-100.
We use networks with about 20, 000 weights to keep
the eigen-decomposition of D(x) ∈ R[d][×][d] tractable. These
networks however possess all the architectural intricacies such
as convolutions, dropout, batch-normalization etc. We evaluate
_D(x) using (2) with the network in evaluation mode._

_A. Highly non-isotropic D(x) for deep networks_

Figs. 1 and 2 show the eigenspectrum[1] of the diffusion
matrix. In all cases, it has a large fraction of almost-zero
eigenvalues with a very small rank that ranges between 0.3% 2%. Moreover, non-zero eigenvalues are spread across a vast
range with a large variance.


datasets have more variety than those in MNIST. Similarly,
while CIFAR-100 has qualitatively similar images as CIFAR10, it has 10 more classes and as a result, it is a much harder
_×_
dataset. This correlates well with the fact that both the mean
and standard-deviation of the eigenvalues in Fig. 2b are much
higher than those in Fig. 2a. Input augmentation increases the
diversity of mini-batch gradients. This is seen in Fig. 2c where
the standard-deviation of the eigenvalues is much higher as
compared to Fig. 2a.

**Remark 15 (Inverse temperature scales with the mean of**
**the eigenspectrum). Remark 14 shows that the mean of the**
eigenspectrum is large if the dataset is diverse. Based on this,
we propose that the inverse temperature β should scale linearly
with the mean of the eigenvalues of D:


_d_ �
## ∑ λ (D)
_k=1_


� _η_

_b_


� [�] 1
_d_


= constant; (14)


(a) MNIST: small-lenet
_λ_ (D) = (0.3 ± 2.11) _×_ 10[−][3]

rank(D) = 1.8%


(b) MNIST: small-fc
_λ_ (D) = (0.9 ± 18.5) _×_ 10[−][3]

rank(D) = 0.6%


Fig. 1: Eigenspectrum of D(x) at three instants during training
(20%, 40% and 100% completion, darker is later). The eigenspectrum
in Fig. 1b for the fully-connected network has a much smaller rank
and much larger variance than the one in Fig. 1a which also performs
better on MNIST. This indicates that convolutional networks are better
conditioned than fully-connected networks in terms of D(x).

**Remark 13 (Noise in SGD is largely independent of the**
**weights). The variance of noise in (3) is**

_η D(xk)_ = 2 β _[−][1]D(xk)._

_b_

We have plotted the eigenspectra of the diffusion matrix
in Fig. 1 and Fig. 2 at three different instants, 20%, 40% and
100% training completion; they are almost indistinguishable.
This implies that the variance of the mini-batch gradients
in deep networks can be considered a constant, highly nonisotropic matrix.

**Remark 14 (More non-isotropic diffusion if data is diverse).**
The eigenspectra in Fig. 2 for CIFAR-10 and CIFAR-100 have
much larger eigenvalues and standard-deviation than those
in Fig. 1, this is expected because the images in the CIFAR

1thresholded at λmax × _d ×_ machine-precision. This formula is widely used,
for instance, in numpy.


where d is the number of weights. This keeps the noise in
SGD constant in magnitude for different values of the learning
rate η, mini-batch size b, architectures, and datasets. Note
that other hyper-parameters which affect stochasticity such as
dropout probability are implicit inside D.

**Remark 16 (Variance of the eigenspectrum informs archi-**
**tecture search). Compare the eigenspectra in Figs. 1a and 1b**
with those in Figs. 2a and 2c. The former pair shows that
small-lenet which is a much better network than small-fc
also has a much larger rank, i.e., the number of non-zero
eigenvalues (D(x) is symmetric). The second pair shows that
for the same dataset, data-augmentation creates a larger variance
in the eigenspectrum. This suggests that both the quantities,
viz., rank of the diffusion matrix and the variance of the
eigenspectrum, inform the performance of a given architecture
on the dataset. Note that as discussed in Remark 15, the mean
of the eigenvalues can be controlled using the learning rate η
and the batch-size b.
This observation is useful for automated architecture search
where we can use the quantity

rank(D)

+ var (λ (D))
_d_

to estimate the efficacy of a given architecture, possibly,
without even training, since D does not depend on the weights
much. This task currently requires enormous amounts of
computational power [20, 21, 22].

_B. Analysis of long-term trajectories_
We train a smaller version of small-fc on 7 7 down-sampled
_×_
MNIST images for 10[5] epochs and store snapshots of the
weights after each epoch to get a long trajectory in the weight
space. We discard the first 10[3] epochs of training (“burnin”)
to ensure that SGD has reached the steady-state. The learning
rate is fixed to 10[−][3] after this, up to 10[5] epochs.

**Remark 17 (Low-frequency periodic components in SGD**
**trajectories). Iterates of SGD, after it reaches the neigh-**


-----

(a) CIFAR-10
_λ_ (D) = 0.27 ± 0.84
rank(D) = 0.34%


(b) CIFAR-100
_λ_ (D) = 0.98 ± 2.16
rank(D) = 0.47%


(c) CIFAR-10: data augmentation
_λ_ (D) = 0.43 ± 1.32
rank(D) = 0.32%


Fig. 2: Eigenspectrum of D(x) at three instants during training (20%, 40% and 100% completion, darker is later). The eigenvalues are much
larger in magnitude here than those of MNIST in Fig. 1, this suggests a larger gradient diversity for CIFAR-10 and CIFAR-100. The diffusion
matrix for CIFAR-100 in Fig. 2b has larger eigenvalues and is more non-isotropic and has a much larger rank than that of Fig. 2a; this
suggests that gradient diversity increases with the number of classes. As Fig. 2a and Fig. 2c show, augmenting input data increases both the
mean and the variance of the eigenvalues while keeping the rank almost constant.

(a) FFT of xk[i] +1 _[−]_ _[x]k[i]_ (b) Auto-correlation (AC) of xk[i] (c) Normalized gradient _[∥][∇]√[f]_ [(]d[x][k][)][∥]

Fig. 3: Fig. 3a shows the Fast Fourier Transform (FFT) of xk[i] +1 _[−]_ _[x]k[i]_ [where][ k][ is the number of epochs and][ i][ denotes the index of the weight.]
Fig. 3b shows the auto-correlation of xk[i] [with][ 99%][ confidence bands denoted by the dotted red lines. Both][ Figs. 3a][ and][ 3b][ show the mean]
and one standard-deviation over the weight index i; the standard deviation is very small which indicates that all the weights have a very
similar frequency spectrum. Figs. 3a and 3b should be compared with the FFT of white noise which should be flat and the auto-correlation of
Brownian motion which quickly decays to zero, respectively. Figs. 3 and 3a therefore show that trajectories of SGD are not simply Brownian
motion. Moreover the gradient at these locations is quite large (Fig. 3c).


borhood of a critical point ∥∇ _f_ (xk)∥≤ _ε, are expected to_
perform Brownian motion with variance var (∇ _fb(x)), the FFT_
in Fig. 3a would be flat if this were so. Instead, we see lowfrequency modes in the trajectory that are indicators of a
periodic dynamics of the force j(x). These modes are not
sharp peaks in the FFT because j(x) can be a non-linear
function of the weights thereby causing the modes to spread
into all dimensions of x. The FFT is dominated by jittery
high-frequency modes on the right with a slight increasing
trend; this suggests the presence of colored noise in SGD at
high-frequencies.
The auto-correlation (AC) in Fig. 3b should be compared
with the AC for Brownian motion which decays to zero very
quickly and stays within the red confidence bands (99%). Our
iterates are significantly correlated with each other even at very
large lags. This further indicates that trajectories of SGD do
not perform Brownian motion.

**Remark 18 (Gradient magnitude in deep networks is**


**always large). Fig. 3c shows that the full-gradient computed**
over the entire dataset (without burnin) does not decrease much
with respect to the number of epochs. While it is expected to
have a non-zero gradient norm because SGD only converges
to a neighborhood of a critical point for non-zero learning
rates, the magnitude of this gradient norm is quite large. This
magnitude drops only by about a factor of 3 over the next 10[5]

epochs. The presence of a non-zero j(x) also explains this, it
causes SGD to be away from critical points, this phenomenon
is made precise in Theorem 22. Let us note that a similar plot
is also seen in [23] for the per-layer gradient magnitude.

V. SGD FOR DEEP NETWORKS IS OUT-OF-EQUILIBRIUM

This section now gives an explicit formula for the potential
Φ(x). We also discuss implications of this for generalization
in Section V-C.
The fundamental difficulty in obtaining an explicit expression
for Φ is that even if the diffusion matrix D(x) is full-rank, there


-----

need not exist a function Φ(x) such that ∇Φ(x) = D[−][1](x) ∇ _f_ (x)
at all x Ω. We therefore split the analysis into two cases:
_∈_

(i) a local analysis near any critical point ∇ _f_ (x) = 0 where
we linearize ∇ _f_ (x) = Fx and ∇Φ(x) = Ux to compute
_U = G[−][1]_ _F for some G, and_
(ii) the general case where ∇Φ(x) cannot be written as a
local rotation and scaling of ∇ _f_ (x).

Let us introduce these cases with an example from [24].

**Example 19 (Double-well potential with limit cycles). De-**
fine

Φ(x) = [(][x]1[2] _[−]_ [1][)][2] + _[x]2[2]_

4 2 _[.]_

Instead of constructing a diffusion matrix D(x), we will directly
construct different gradients ∇ _f_ (x) that lead to the same
potential Φ; these are equivalent but the later is much easier.
_√_
The dynamics is given by dx = ∇ _f_ (x) dt + 2 dW (t), where
_−_

∇ _f_ (x) = _j(x) + ∇Φ(x). We pick j = λ_ _e[Φ]_ _J[ss](x) for some_
_−_
parameter λ > 0 where

(x1[2][+][x]2[2][)][2]
_J[ss](x) = e[−]_ 4 (−x2, x1).


Note that this satisfies (6) and does not change ρ [ss] = e[−][Φ].
Fig. 4 shows the gradient field f (x) along with a discussion.

_A. Linearization around a critical point_

Without loss of generality, let x = 0 be a critical point of
_f_ (x). This critical point can be a local minimum, maximum,
or even a saddle point. We linearize the gradient around the
origin and define a fixed matrix F ∈ R[d][×][d] (the Hessian) to be
∇ _f_ (x) = Fx. Let D = D(0) be the constant diffusion matrix
matrix. The dynamics in (3) can now be written as


_B. General case_

We next give the general expression for the deviation of the
critical points ∇Φ from those of the original loss ∇ _f_ .
**A-type stochastic integration: A Fokker-Planck equation**
is a deterministic partial differential equation (PDE) and every
steady-state distribution, ρ [ss] ∝ _e[−][β]_ [Φ] in this case, has a unique
such PDE that achieves it. However, the same PDE can be
tied to different SDEs depending on the stochastic integration
scheme, e.g., Ito, Stratonovich [2, 26], Hanggi [27], α-type
etc. An “A-type” interpretation is one such scheme [28, 29].
It is widely used in non-equilibrium studies in physics and
biology [30, 31] because it allows one to compute the steadystate distribution easily; its implications are supported by other
mathematical analyses such as [32, 5].
The main result of the section now follows. It exploits the
A-type interpretation to compute the difference between the
most likely locations of SGD which are given by the critical
points of the potential Φ(x) and those of the original loss f (x).

**Theorem 22 (Most likely locations are not the critical**
**points of the loss). The Ito SDE**

�
_dx = −∇_ _f_ (x) dt + 2β _[−][1]D(x) dW_ (t)

_is equivalent to the A-type SDE [28, 29]_


�
_dx =_ _Fx dt +_
_−_


2β _[−][1]_ _D dW_ (t). (15)


� � �
_dx = −_ _D(x)+_ _Q(x)_ ∇Φ(x) dt + 2β _[−][1]D(x) dW_ (t) (18)

_with the same steady-state distribution ρ_ [ss] ∝ _e[−][β]_ [Φ][(][x][)] _and_
_Fokker-Planck equation (FP) if_

� � � �
∇ _f_ (x) = _D(x)+_ _Q(x)_ ∇Φ(x) _−_ _β_ _[−][1]∇_ _·_ _D(x)+_ _Q(x)_ _._
(19)
_The anti-symmetric matrix Q(x) and the potential Φ(x) can_
_be explicitly computed in terms of the gradient ∇_ _f_ (x) and the
_diffusion matrix D(x). The potential Φ(x) does not depend on_
_the inverse temperature β_ _._

The proof exploits the fact that the the Ito SDE (3) and the Atype SDE (18) should have the same Fokker-Planck equations
because they have the same steady-state distributions.

**Remark 23 (SGD is far away from critical points). The**
time spent by a Markov chain at a state x is proportional
to its steady-state distribution ρ [ss](x). While it is easily seen
that SGD does not converge in the Cauchy sense due to the
stochasticity, it is very surprising that it may spend a significant
amount of time away from the critical points of the original
loss. If D(x)+ _Q(x) has a large divergence, the set of states_
with ∇Φ(x) = 0 might be drastically different than those with
∇ _f_ (x) = 0. This is also seen in example Fig. 4c; in fact, SGD
may even converge around a saddle point.

This also closes the logical loop we began in Section III
where we assumed the existence of ρ [ss] and defined the potential
Φ using it. Lemma 20 and Theorem 22 show that both can be
defined uniquely in terms of the original quantities, i.e., the
gradient term ∇ _f_ (x) and the diffusion matrix D(x). There is
no ambiguity as to whether the potential Φ(x) results in the


**Lemma 20 (Linearization). The matrix F in (15) can be**
_uniquely decomposed into_

_F = (D_ + _Q) U;_ (16)

_D and Q are the symmetric and anti-symmetric parts of a_
_matrix G with GF_ _[⊤]_ _−_ _FG[⊤]_ = 0, to get Φ(x) = [1]2 _[x][⊤][Ux.]_

The above lemma is a classical result if the critical point is a
local minimum, i.e., if the loss is locally convex near x = 0; this
case has also been explored in machine learning before [14].
We refer to [25] for the proof that linearizes around any critical
point.

**Remark 21 (Rotation of gradients). We see from Lemma 20**
that, near a critical point,

∇ _f = (D_ + _Q) ∇Φ_ _−_ _β_ _[−][1]∇_ _·_ _D_ _−_ _β_ _[−][1]∇_ _·_ _Q_ (17)

up to the first order. This suggests that the effect of j(x) is to
rotate the gradient field and move the critical points, also seen
in Fig. 4b. Note that ∇ _D = 0 and ∇_ _Q = 0 in the linearized_

_·_ _·_
analysis.


-----

(a) λ = 0 (b) λ = 0.5 (c) λ = 1.5

Fig. 4: Gradient field for the dynamics in Example 19: line-width is proportional to the magnitude of the gradient ∥∇ _f_ (x)∥, red dots denote
the most likely locations of the steady-state e[−][Φ] while the potential Φ is plotted as a contour map. The critical points of f (x) and Φ(x) are
the same in Fig. 4a, namely (±1, 0), because the force j(x) = 0. For λ = 0.5 in Fig. 4b, locations where ∇ _f_ (x) = 0 have shifted slightly as
predicted by Theorem 22. The force field also has a distinctive rotation component, see Remark 21. In Fig. 4c with a large ∥ _j(x)∥, SGD_
converges to limit cycles around the saddle point at the origin. This is highly surprising and demonstrates that the solutions obtained by SGD
may be very different from local minima.


steady-state ρ [ss](x) or vice-versa.

**Remark 24 (Consistent with the linear case). Theorem 22**
presents a picture that is completely consistent with Lemma 20.
If j(x) = 0 and Q(x) = 0, or if Q is a constant like the linear
case in Lemma 20, the divergence of Q(x) in (19) is zero.

**Remark 25 (Out-of-equilibrium effect can be large even**
**if D is constant). The presence of a Q(x) with non-zero**
divergence is the consequence of a non-isotropic D(x) and it
persists even if D is constant and independent of weights
_x. So long as D is not isotropic, as we discussed in the_
beginning of Section V, there need not exist a function Φ(x)
such that ∇Φ(x) = D[−][1] ∇ _f_ (x) at all x. This is also seen in
our experiments, the diffusion matrix is almost constant with
respect to weights for deep networks, but consequences of
out-of-equilibrium behavior are still seen in Section IV-B.

**Remark 26 (Out-of-equilibrium effect increases with β** _[−][1])._
The effect predicted by (19) becomes more pronounced if
_β_ _[−][1]_ = 2[η]b [is large. In other words, small batch-sizes or high]

learning rates cause SGD to be drastically out-of-equilibrium.
Theorem 5 also shows that as β _[−][1]_ _→_ 0, the implicit entropic
regularization in SGD vanishes. Observe that these are exactly
the conditions under which we typically obtain good generalization performance for deep networks [15, 16]. This suggests
that non-equilibrium behavior in SGD is crucial to obtain good
generalization performance, especially for high-dimensional
models such as deep networks where such effects are expected
to be more pronounced.

_C. Generalization_

It was found that solutions of discrete learning problems that
generalize well belong to dense clusters in the weight space [33,
34]. Such dense clusters are exponentially fewer compared to
isolated solutions. To exploit these observations, the authors
proposed a loss called “local entropy” that is out-of-equilibrium
by construction and can find these well-generalizable solutions
easily. This idea has also been successful in deep learning


where [35] modified SGD to seek solutions in “wide minima”
with low curvature to obtain improvements in generalization
performance as well as convergence rate [36].
Local entropy is a smoothed version of the original loss
given by
�
_fγ_ (x) = − log _Gγ ∗_ _e[−]_ _[f]_ [(][x][)][�] _,_

where Gγ is a Gaussian kernel of variance γ. Even with an
isotropic diffusion matrix, the steady-state distribution with
_fγ_ (x) as the loss function is ργ[ss][(][x][)][ ∝] _[e][−][β][ f][γ]_ [(][x][)][. For large values]
of γ, the new loss makes the original local minima exponentially
less likely. In other words, local entropy does not rely on nonisotropic gradient noise to obtain out-of-equilibrium behavior,
it gets it explicitly, by construction. This is also seen in Fig. 4c:
if SGD is drastically out-of-equilibrium, it converges around
the “wide” saddle point region at the origin which has a small
local entropy.
Actively constructing out-of-equilibrium behavior leads to
good generalization in practice. Our evidence that SGD on
deep networks itself possesses out-of-equilibrium behavior then
indicates that SGD for deep networks generalizes well because
of such behavior.

VI. RELATED WORK

**SGD, variational inference and implicit regularization**
The idea that SGD is related to variational inference has been
seen in machine learning before [37, 14] under assumptions
such as quadratic steady-states; for instance, see [38] for
methods to approximate steady-states using SGD. Our results
here are very different, we would instead like to understand
properties of SGD itself. Indeed, in full generality, SGD
performs variational inference using a new potential Φ that it
implicitly constructs given an architecture and a dataset.
It is widely believed that SGD is an implicit regularizer,
see [39, 40, 23] among others. This belief stems from its
remarkable empirical performance. Our results show that such
intuition is very well-placed. Thanks to the special architecture
of deep networks where gradient noise is highly non-isotropic,


-----

SGD helps itself to a potential Φ with properties that lead to
both generalization and acceleration.
**SGD and noise: Noise is often added in SGD to improve**
its behavior around saddle points for non-convex losses,
see [41, 42, 43]. It is also quite indispensable for training deep
networks [44, 45, 46, 47, 12]. There is however a disconnect
between these two directions due to the fact that while adding
external gradient noise helps in theory, it works poorly in
practice [48, 49]. Instead, “noise tied to the architecture” works
better, e.g., dropout, or small mini-batches. Our results close
this gap and show that SGD crucially leverages the highly
degenerate noise induced by the architecture.
**Gradient diversity [50] construct a scalar measure of the**
gradient diversity given by ∑k∥∇ _fk(x)∥/∥∇_ _f_ (x)∥, and analyze
its effect on the maximum allowed batch-size in the context
of distributed optimization.
**Markov Chain Monte Carlo MCMC methods that sample**
from a negative log-likelihood Φ(x) have employed the idea
of designing a force j = ∇Φ ∇ _f to accelerate convergence,_
_−_
see [51] for a thorough survey, or [52, 53] for a rigorous
treatment. We instead compute the potential Φ given ∇ _f and_
_D, which necessitates the use of techniques from physics. In_
fact, our results show that since j = 0 for deep networks due
_̸_
to non-isotropic gradient noise, very simple algorithms such
as SGLD by [54] also benefit from the acceleration that their
sophisticated counterparts aim for [55, 56].

VII. DISCUSSION

The continuous-time point-of-view used in this paper gives
access to general principles that govern SGD, such analyses are
increasingly becoming popular [57, 58]. However, in practice,
deep networks are trained for only a few epochs with discretetime updates. Closing this gap is an important future direction.
A promising avenue towards this is that for typical conditions
in practice such as small mini-batches or large learning rates,
SGD converges to the steady-state distribution quickly [59].

VIII. ACKNOWLEDGMENTS

PC would like to thank Adam Oberman for introducing
him to the JKO functional. The authors would also like
to thank Alhussein Fawzi for numerous discussions during
the conception of this paper and his contribution to its
improvement.

REFERENCES

[1] Pratik Chaudhari and Stefano Soatto. Stochastic gradient descent performs
variational inference, converges to limit cycles for deep networks.
_arXiv:1710.11029, 2017._

[2] Hannes Risken. The Fokker-Planck Equation. Springer, 1996.

[3] Qianxiao Li, Cheng Tai, and E Weinan. Stochastic modified equations
and adaptive stochastic gradient algorithms. In ICML, pages 2101–2110,
2017.

[4] Hans Ottinger. Beyond equilibrium thermodynamics. John Wiley & Sons,
2005.

[5] Hong Qian. The zeroth law of thermodynamics and volume-preserving
conservative system in equilibrium with stochastic damping. Physics
_Letters A, 378(7):609–616, 2014._

[6] Richard Jordan, David Kinderlehrer, and Felix Otto. Free energy and
the fokker-planck equation. Physica D: Nonlinear Phenomena, 107(24):265–271, 1997.



[7] Filippo Santambrogio. Optimal transport for applied mathematicians.
_Birkuser, NY, 2015._

[8] Cedric Villani.´ _Optimal transport: old and new, volume 338. Springer_
Science & Business Media, 2008.

[9] Filippo Santambrogio. Euclidean, metric, and Wasserstein gradient flows:
an overview. Bulletin of Mathematical Sciences, 7(1):87–154, 2017.

[10] Diederik P Kingma and Max Welling. Auto-encoding variational Bayes.
_arXiv:1312.6114, 2013._

[11] Naftali Tishby, Fernando C. Pereira, and William Bialek. The information
bottleneck method. In Proc. of the 37-th Annual Allerton Conference on
_Communication, Control and Computing, pages 368–377, 1999._

[12] Alessandro Achille and Stefano Soatto. On the emergence of invariance
and disentangling in deep representations. arXiv:1706.01350, 2017.

[13] Michael I Jordan, Zoubin Ghahramani, Tommi S Jaakkola, and
Lawrence K Saul. An introduction to variational methods for graphical
models. Machine learning, 37(2):183–233, 1999.

[14] Stephan Mandt, Matthew Hoffman, and David Blei. A variational analysis
of stochastic gradient algorithms. In ICML, pages 354–363, 2016.

[15] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail
Smelyanskiy, and Ping Tak Peter Tang. On large-batch training for deep
learning: Generalization gap and sharp minima. arXiv:1609.04836, 2016.

[16] Priya Goyal, Piotr Dollr, Ross Girshick, Pieter Noordhuis, Lukasz
Wesolowski, Aapo Kyrola, Andrew Tulloch, Yangqing Jia, and Kaiming
He. Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour.
_arXiv:1706.02677, 2017._

[17] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning
applied to document recognition. Proceedings of the IEEE, 86(11):2278–
2324, 1998.

[18] A. Krizhevsky. Learning multiple layers of features from tiny images.
Master’s thesis, Computer Science, University of Toronto, 2009.

[19] J. Springenberg, A. Dosovitskiy, T. Brox, and M. Riedmiller. Striving
for simplicity: The all convolutional net. arXiv:1412.6806, 2014.

[20] Barret Zoph and Quoc V Le. Neural architecture search with reinforcement learning. arXiv:1611.01578, 2016.

[21] Bowen Baker, Otkrist Gupta, Nikhil Naik, and Ramesh Raskar. Designing neural network architectures using reinforcement learning.
_arXiv:1611.02167, 2016._

[22] Andrew Brock, Theodore Lim, JM Ritchie, and Nick Weston.
SMASH: One-Shot Model Architecture Search through HyperNetworks.
_arXiv:1708.05344, 2017._

[23] Ravid Shwartz-Ziv and Naftali Tishby. Opening the black box of deep
neural networks via information. arXiv:1703.00810, 2017.

[24] Jae Dong Noh and Joongul Lee. On the steady-state probability
distribution of nonequilibrium stochastic systems. Journal of the Korean
_Physical Society, 66(4):544–552, 2015._

[25] Chulan Kwon, Ping Ao, and David J Thouless. Structure of stochastic
dynamics near fixed points. Proceedings of the National Academy of
_Sciences of the United States of America, 102(37):13029–13033, 2005._

[26] Bernt Oksendal. Stochastic differential equations. Springer, 2003.

[27] P Hanggi.¨ On derivations and solutions of master equations and
asymptotic representations. Zeitschrift fur Physik B Condensed Matter¨,
30(1):85–95, 1978.

[28] Ping Ao, Chulan Kwon, and Hong Qian. On the existence of potential
landscape in the evolution of complex systems. Complexity, 12(4):19–27,
2007.

[29] Jianghong Shi, Tianqi Chen, Ruoshi Yuan, Bo Yuan, and Ping Ao.
Relation of a new interpretation of stochastic differential equations to
ito process. Journal of Statistical physics, 148(3):579–590, 2012.

[30] Jin Wang, Li Xu, and Erkang Wang. Potential landscape and flux
framework of nonequilibrium networks: robustness, dissipation, and
coherence of biochemical oscillations. _Proceedings of the National_
_Academy of Sciences, 105(34):12271–12276, 2008._

[31] X-M Zhu, L Yin, L Hood, and P Ao. Calculating biological behaviors
of epigenetic states in the phage λ life cycle. Functional & integrative
_genomics, 4(3):188–195, 2004._

[32] T Tel, R Graham, and G Hu. Nonequilibrium potentials and their powerseries expansions. Physical Review A, 40(7):4065, 1989.

[33] Carlo Baldassi, Alessandro Ingrosso, Carlo Lucibello, Lucibello Saglietti,
and Riccardo Zecchina. Subdominant dense clusters allow for simple
learning and high computational performance in neural networks with
discrete synapses. Physical review letters, 115(12):128101, 2015.

[34] C. Baldassi, C. Borgs, J. Chayes, A. Ingrosso, C. Lucibello, L. Saglietti,
and R. Zecchina. Unreasonable effectiveness of learning neural networks:
From accessible states and robust ensembles to basic algorithmic schemes.


-----

_PNAS, 113(48):E7655–E7662, 2016._

[35] Pratik Chaudhari, Anna Choromanska, Stefano Soatto, Yann LeCun,
Carlo Baldassi, Christian Borgs, Jennifer Chayes, Levent Sagun, and
Riccardo Zecchina. Entropy-SGD: biasing gradient descent into wide
valleys. arXiv:1611.01838, 2016.

[36] Pratik Chaudhari, Carlo Baldassi, Riccardo Zecchina, Stefano Soatto,
Ameet Talwalkar, and Adam Oberman. Parle: parallelizing stochastic
gradient descent. arXiv:1707.00424, 2017.

[37] David Duvenaud, Dougal Maclaurin, and Ryan Adams. Early stopping
as non-parametric variational inference. In AISTATS, pages 1070–1077,
2016.

[38] Stephan Mandt, Matthew D Hoffman, and David M Blei. Stochastic
Gradient Descent as Approximate Bayesian Inference. arXiv:1704.04289,
2017.

[39] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol
Vinyals. Understanding deep learning requires rethinking generalization.
_arXiv:1611.03530, 2016._

[40] Behnam Neyshabur, Ryota Tomioka, Ruslan Salakhutdinov, and Nathan
Srebro. Geometry of optimization and implicit regularization in deep
learning. arXiv:1705.03071, 2017.

[41] Jason D Lee, Max Simchowitz, Michael I Jordan, and Benjamin Recht.
Gradient descent only converges to minimizers. In COLT, pages 1246–
1257, 2016.

[42] Animashree Anandkumar and Rong Ge. Efficient approaches for escaping
higher order saddle points in non-convex optimization. In COLT, pages
81–102, 2016.

[43] Rong Ge, Furong Huang, Chi Jin, and Yang Yuan. Escaping from saddle
points online stochastic gradient for tensor decomposition. In COLT,
pages 797–842, 2015.

[44] Geoffrey E Hinton and Drew Van Camp. Keeping the neural networks
simple by minimizing the description length of the weights. In
_Proceedings of the sixth annual conference on Computational learning_
_theory, pages 5–13. ACM, 1993._

[45] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and
Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks
from overfitting. JMLR, 15(1):1929–1958, 2014.

[46] Diederik P Kingma, Tim Salimans, and Max Welling. Variational dropout
and the local reparameterization trick. In NIPS, pages 2575–2583, 2015.

[47] Caglar Gulcehre, Marcin Moczulski, Misha Denil, and Yoshua Bengio.
Noisy activation functions. In ICML, pages 3059–3068, 2016.

[48] Arvind Neelakantan, Luke Vilnis, Quoc V Le, Ilya Sutskever, Lukasz
Kaiser, Karol Kurach, and James Martens. Adding gradient noise
improves learning for very deep networks. arXiv:1511.06807, 2015.

[49] Pratik Chaudhari and Stefano Soatto. On the energy landscape of deep
networks. arXiv:1511.06485, 2015.

[50] Dong Yin, Ashwin Pananjady, Max Lam, Dimitris Papailiopoulos, Kannan
Ramchandran, and Peter Bartlett. Gradient diversity empowers distributed
learning. arXiv:1706.05699, 2017.

[51] Yi-An Ma, Tianqi Chen, and Emily Fox. A complete recipe for stochastic
gradient MCMC. In NIPS, pages 2917–2925, 2015.

[52] Grigorios A Pavliotis. Stochastic processes and applications. Springer,
2016.

[53] Marcus Kaiser, Robert L Jack, and Johannes Zimmer. Acceleration
of convergence to equilibrium in Markov chains by breaking detailed
balance. Journal of Statistical Physics, 168(2):259–287, 2017.

[54] Max Welling and Yee W Teh. Bayesian learning via stochastic gradient
Langevin dynamics. In ICML, pages 681–688, 2011.

[55] Nan Ding, Youhan Fang, Ryan Babbush, Changyou Chen, Robert Skeel,
and Hartmut Neven. Bayesian sampling using stochastic gradient
thermostats. In NIPS, pages 3203–3211, 2014.

[56] Changyou Chen, David Carlson, Zhe Gan, Chunyuan Li, and Lawrence
Carin. Bridging the gap between stochastic gradient MCMC and
stochastic optimization. In AISTATS, pages 1051–1060, 2016.

[57] Andre Wibisono, Ashia C Wilson, and Michael I Jordan. A variational
perspective on accelerated methods in optimization. _PNAS, page_
201614734, 2016.

[58] Pratik Chaudhari, Adam Oberman, Stanley Osher, Stefano Soatto, and
Carlier Guillame. Deep Relaxation: partial differential equations for
optimizing deep neural networks. arXiv:1704.04932, 2017.

[59] Maxim Raginsky, Alexander Rakhlin, and Matus Telgarsky. Non-convex
learning via Stochastic Gradient Langevin Dynamics: a nonasymptotic
analysis. arXiv:1702.03849, 2017.

[60] Chris Junchi Li, Lei Li, Junyang Qian, and Jian-Guo Liu. Batch size
matters: A diffusion approximation framework on nonconvex stochastic


gradient descent. arXiv:1705.07562, 2017.

[61] Ilya Prigogine. Thermodynamics of irreversible processes, volume 404.
Thomas, 1955.

[62] Lars Onsager. Reciprocal relations in irreversible processes. I. Physical
_review, 37(4):405, 1931._

[63] Lars Onsager. Reciprocal relations in irreversible processes. II. Physical
_review, 38(12):2265, 1931._

[64] Till Daniel Frank. Nonlinear Fokker-Planck equations: fundamentals
_and applications. Springer Science & Business Media, 2005._

[65] Edwin T Jaynes. The minimum entropy production principle. Annual
_Review of Physical Chemistry, 31(1):579–601, 1980._

APPENDIX

_A. Diffusion matrix D(x)_

In this section we denote gk := ∇ _fk(x) and g := ∇_ _f_ (x) =
1
_N_ [∑]k[N]=1 _[g][k][. Although we drop the dependence of][ g][k][ on][ x][ to]_
keep the notation clear, we emphasize that the diffusion matrix
_D depends on the weights x._
_1) With replacement: Let i1,...,_ _ib be b iid random variables_
in {1, 2,..., _N}. We would like to compute_

� 1 _b_ �

var ∑ _gi_ _j_

_b_ _j=1_

⎧⎨� 1 _b_ �� 1 _b_ �⊤[⎫]⎬

= Ei1,...,ib ⎩ _b_ _j∑=1_ _gi_ _j −_ _g_ _b_ _j∑=1_ _gi_ _j −_ _g_ ⎭ _[.]_

Note that we have that for any j ̸= k, the random vectors gi _j_
and gik are independent. We therefore have

�
covar(gi j _,_ _gik_ ) = 0 = Ei _j, ik_ (gi _j −_ _g)(gik −_ _g)[⊤][�]_

We use this to obtain


covar(1i∈b, **1** _j∈b) = −_ _N[b][2][(]([N]N[ −]_ _[b]1[)])_ _[.]_

_−_


= [1]

_b[2]_


_b_
## ∑ gi j
_j=1_


�


_b_
## ∑ var(gi j )
_j=1_


var


�
1
_b_


= [1]

_N_ _b_


= [1]

_b_


_N_

�

## ∑ (gk − g) (gk − g)[⊤][�]
_k=1_

� �
∑[N]k=1 _[g][k][ g]k[⊤]_
_g g[⊤]_ _._
_−_
_N_


We will set


_D(x) =_ [1]

_N_


� _N_
## ∑ gk g[⊤]k
_k=1_


�


_g g[⊤]._ (A1)
_−_


and assimilate the factor of b[−][1] in the inverse temperature β .
_2) Without replacement: Let us define an indicator random_
variable 1i∈b that denotes if an example i was sampled in batch
_b. We can show that_

var(1i∈b) = _N[b]_ _N[2][,]_

_[−]_ _[b][2]_


and for i = j,
_̸_


-----

Similar to [60], we can now compute


�
1
_b_


�


� 1 _N_ �

var _b_ _k∑=1_ _gk 1k∈b_

� _N_

= _b[1][2][ var]_ _k∑=1_ _gk 1k∈b_


�


_C. Some properties of the force j_

The Fokker-Planck equation (FP) can be written in terms of
the probability current as

0 = ρt[ss] [=][ ∇] _[·]_ �− _j ρ_ [ss] + _D ∇Φ ρ_ [ss] _−_ _β_ _[−][1](∇_ _·_ _D) ρ_ [ss] + _β_ _[−][1]∇_ _·_ (Dρ [ss])�

= ∇ _J[ss]._

_·_

Since we have ρ [ss] ∝ _e[−][β]_ [Φ][(][x][)], from the observation (7), we also
have that

0 = ρt[ss] [=][ ∇] _[·]_ �D ∇Φ ρ [ss] + _β_ _[−][1]D ∇ρ_ [ss][�] _,_

and consequently,


0 = ∇ ( _j ρ_ [ss])

_·_

(A4)

_j(x) =_ _[J][ss]_
_⇒_

_ρ_ [ss][ .]

In other words, the conservative force is non-zero only if
detailed balance is broken, i.e., J[ss] = 0. We also have
_̸_

0 = ∇ ( _j ρ_ [ss])

_·_

= ρ [ss] (∇ _j_ _j_ ∇Φ) _,_

_·_ _−_ _·_

which shows using Assumption 4 and ρ [ss](x) > 0 for all x Ω
_∈_
that j(x) is always orthogonal to the gradient of the potential

0 = j(x) ∇Φ(x)

_·_

(A5)
= j(x) ∇ρ [ss].

_·_

Using the definition of j(x) in (8), we have detailed balance
when
∇ _f_ (x) = D(x) ∇Φ(x) _−_ _β_ _[−][1]∇_ _·_ _D(x)._ (A6)


= [1]

_b[2]_

= [1]

_b_


_N_
## ∑ gk g[⊤]k [var][(][1][k][∈][b][)+][ 1]
_k=1_ _b[2]_


�
1
_−_ _[b]_

_N_


_N_

_[⊤]k_ [var][(][1][k][∈][b][)+][ 1] ∑ _gi g[⊤]j_ [covar][(][1][i][∈][b][,] **[1][ j][∈][b][)]**

_b[2]_ _i, j=1, i≠_ _j_

� [�] ∑[N]k=1 _[g][k][ g]k[⊤]_ � 1 � �
1 _g g[⊤]_ _._
_−_ _−_
_N_ 1 _N_ 1
_−_ _−_


We will again set

1
_D(x) =_
_N_ 1
_−_


� _N_
## ∑ gk g[⊤]k
_k=1_


�


� 1
1
_−_ _−_
_N_ 1
_−_


�
_g g[⊤]_ (A2)


and assimilate the factor of b[−][1][ �]1 _−_ _N[b]_ � that depends on the

batch-size in the inverse temperature β .

_B. Discussion on Assumption 4_

The definition of the conservative force j(x) in (8) and
the free energy (11) allows us to rewrite the Fokker-Planck
equation (FP) as


� � _δ_ _F_
_ρt = ∇_ _·_ _−_ _j ρ +_ _ρ D ∇_

_δρ_


��
_._ (A3)


Let F(ρ) be as defined in (11). In non-equilibrium thermodynamics, it is assumed that the local entropy production is a
product of the force −∇ � _δδρF_ � from (A3) and the probability
current _J(x,t) from (FP). This assumption in this form was_
_−_
first introduced by [61] based on the works of [62, 63]. See [64,
Sec. 4.5] for a mathematical treatment and [65] for further
discussion. The rate of entropy (Si) increase is given by


� � _δ_ _F_

_β_ _[−][1][ dS][i]_

_dt_ [=] _x∈Ω_ [∇] _δρ_


�
_J(x,t) dx._


This can now be written using (A3) again as


� �

_β_ _[−][1][ dS][i]_ _ρ D :_ ∇ _[δ]_ _[F]_

_dt_ [=] _δρ_


��
∇ _[δ]_ _[F]_

_δρ_


�⊤ � �
+ _jρ_ ∇ _[δ]_ _[F]_

_δρ_


�
_dx._


The first term in the above expression is non-negative, in order
to ensure that _[dS]dt[i]_ _[≥]_ [0, we require]

� � �
0 = _jρ_ ∇ _[δ]_ _[F]_ _dx_

_δρ_

� � _δ_ _F_ �
= ∇ ( _jρ)_ _dx;_

_·_

_δρ_

where the second equality again follows by integration by
parts. It can be shown [64, Sec. 4.5.5] that the condition
in Assumption 4, viz., ∇ _j(x) = 0, is sufficient to make the_

_·_
above integral vanish and therefore for the entropy generation
to be non-negative.


-----

