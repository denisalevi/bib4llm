# Citation Key: Chaudhari2018

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



---

## STOCHASTIC GRADIENT DESCENT PERFORMS VARIATIONAL
#### INFERENCE, CONVERGES TO LIMIT CYCLES FOR DEEP NETWORKS

**Pratik Chaudhari, Stefano Soatto**


Computer Science, University of California, Los Angeles.

[Email: pratikac@ucla.edu, soatto@ucla.edu](mailto:pratikac@ucla.edu)


### ABSTRACT

Stochastic gradient descent (SGD) is widely believed to perform implicit
regularization when used to train deep neural networks, but the precise manner
in which this occurs has thus far been elusive. We prove that SGD minimizes an
average potential over the posterior distribution of weights along with an entropic
regularization term. This potential is however not the original loss function in
general. So SGD does perform variational inference, but for a different loss than
the one used to compute the gradients. Even more surprisingly, SGD does not even
converge in the classical sense: we show that the most likely trajectories of SGD
for deep networks do not behave like Brownian motion around critical points.
Instead, they resemble closed loops with deterministic components. We prove
that such “out-of-equilibrium” behavior is a consequence of highly non-isotropic
gradient noise in SGD; the covariance matrix of mini-batch gradients for deep
networks has a rank as small as 1% of its dimension. We provide extensive
empirical validation of these claims, proven in the appendix.


**Keywords: deep networks, stochastic gradient descent, variational inference, gradient**
noise, out-of-equilibrium, thermodynamics, Wasserstein metric, Fokker-Planck equation,
wide minima, Markov chain Monte Carlo

### 1 INTRODUCTION


Our first result is to show precisely in what sense stochastic gradient descent (SGD) implicitly
performs variational inference, as is often claimed informally in the literature. For a loss function
_f_ (x) with weights x ∈ R[d], if ρ [ss] is the steady-state distribution over the weights estimated by SGD,

� �
_ρ_ [ss] = arg minρ E x∼ρ Φ(x) _−_ 2[η]b _[H][(][ρ][)][;]_


where H(ρ) is the entropy of the distribution ρ and η and b are the learning rate and batch-size,
respectively. The potential Φ(x), which we characterize explicitly, is related but not necessarily equal
to f (x). It is only a function of the architecture and the dataset. This implies that SGD implicitly
performs variational inference with a uniform prior, albeit of a different loss than the one used to
compute back-propagation gradients.

We next prove that the implicit potential Φ(x) is equal to our chosen loss f (x) if and only if the
noise in mini-batch gradients is isotropic. This condition, however, is not satisfied for deep networks.
Empirically, we find gradient noise to be highly non-isotropic with the rank of its covariance matrix
being about 1% of its dimension. Thus, SGD on deep networks implicitly discovers locations where
∇Φ(x) = 0, these are not the locations where ∇ _f_ (x) = 0. This is our second main result: the most
likely locations of SGD are not the local minima, nor the saddle points, of the original loss. The
deviation of these critical points, which we compute explicitly scales linearly with η/b and is
typically large in practice.


-----

When mini-batch noise is non-isotropic, SGD does not even converge in the classical sense. We
prove that, instead of undergoing Brownian motion in the vicinity of a critical point, trajectories have
a deterministic component that causes SGD to traverse closed loops in the weight space. We detect
such loops using a Fourier analysis of SGD trajectories. We also show through an example that SGD
with non-isotropic noise can even converge to stable limit cycles around saddle points.

### 2 BACKGROUND ON CONTINUOUS-TIME SGD

Stochastic gradient descent performs the following updates while training a network xk+1 = xk −
_η ∇_ _fb(xk) where η is the learning rate and ∇_ _fb(xk) is the average gradient over a mini-batch b,_

∇ _fb(x) =_ [1] ∇ _fk(x)._ (1)

_b_ _k[∑]∈b_

We overload notation b for both the set of examples in a mini-batch and its size. We assume that
weights belong to a compact subset Ω _⊂_ R[d], to ensure appropriate boundary conditions for the
evolution of steady-state densities in SGD, although all our results hold without this assumption if
the loss grows unbounded as ∥x∥→ ∞, for instance, with weight decay as a regularizer.

**Definition 1 (Diffusion matrix D(x)). If a mini-batch is sampled with replacement, we show**
in Appendix A.1 that the variance of mini-batch gradients is var (∇ _fb(x)) =_ _[D][(]b[x][)]_ where


�
1

_D(x) =_

_N_


_N_ �
∇ _fk(x) ∇_ _fk(x)[⊤]_
## ∑
_k=1_


_−_ ∇ _f_ (x) ∇ _f_ (x)[⊤] _⪰_ 0. (2)


Note that D(x) is independent of the learning rate η and the batch-size b. It only depends on the
weights x, architecture and loss defined by f (x), and the dataset. We will often discuss two cases:
isotropic diffusion when D(x) is a scalar multiple of identity, independent of x, and non-isotropic
diffusion, when D(x) is a general function of the weights x.

We now construct a stochastic differential equation (SDE) for the discrete-time SGD updates.

**Lemma 2 (Continuous-time SGD). The continuous-time limit of SGD is given by**

�
_dx(t) = −∇_ _f_ (x) dt + 2β _[−][1]D(x) dW_ (t); (3)


_where W_ (t) is Brownian motion and β is the inverse temperature defined as β _[−][1]_ = 2[η]b[. The steady-]

_state distribution of the weights ρ(z,t) ∝_ P�x(t) = z�, evolves according to the Fokker-Planck
_equation (Risken, 1996, Ito form):_

_∂ρ∂t_ [=][ ∇] _[·]_ �∇ _f_ (x) ρ + _β_ _[−][1]_ ∇ _·_ �D(x) ρ�[�] (FP)

_where the notation ∇_ _· v denotes the divergence ∇_ _· v = ∑i ∂xi vi(x) for any vector v(x) ∈_ R[d]; the
_divergence operator is applied column-wise to matrices such as D(x)._

We refer to Li et al. (2017b, Thm. 1) for the proof of the convergence of discrete SGD to (3). Note
that β _[−][1]_ completely captures the magnitude of noise in SGD that depends only upon the learning
rate η and the mini-batch size b.

**Assumption 3 (Steady-state distribution exists and is unique). We assume that the steady-state**
distribution of the Fokker-Planck equation (FP) exists and is unique, this is denoted by ρ [ss](x) and
satisfies,

0 = _[∂ρ]_ [ss] = ∇ _·_ �∇ _f_ (x) ρ [ss] + _β_ _[−][1]_ ∇ _·_ �D(x) ρ [ss][��]. (4)

_∂t_


-----

### 3 SGD PERFORMS VARIATIONAL INFERENCE

Let us first implicitly define a potential Φ(x) using the steady-state distribution ρ [ss]:

Φ(x) = −β _[−][1]_ log _ρ_ [ss](x), (5)

up to a constant. The potential Φ(x) depends only on the full-gradient and the diffusion matrix;
see Appendix C for a proof. It will be made explicit in Section 5. We express ρ [ss] in terms of the
potential using a normalizing constant Z(β ) as

1
_ρ_ [ss](x) = (6)
_Z(β_ ) _[e][−][β]_ [Φ][(][x][)]

which is also the steady-state solution of

�
_dx = β_ _[−][1]_ ∇ _·_ _D(x) dt −_ _D(x) ∇Φ(x) dt +_ 2β _[−][1]D(x) dW_ (t) (7)

as can be verified by direct substitution in (FP).

The above observation is very useful because it suggests that, if ∇ _f_ (x) can be written in terms of
the diffusion matrix and a gradient term ∇Φ(x), the steady-state distribution of this SDE is easily
obtained. We exploit this observation to rewrite ∇ _f_ (x) in terms a term D ∇Φ that gives rise to the
above steady-state, the spatial derivative of the diffusion matrix, and the remainder:

_j(x) = −∇_ _f_ (x)+ _D(x) ∇Φ(x)_ _−_ _β_ _[−][1]∇_ _·_ _D(x),_ (8)

interpreted as the part of ∇ _f_ (x) that cannot be written as D Φ[′](x) for some Φ[′]. We now make an
important assumption on j(x) which has its origins in thermodynamics.

**Assumption 4 (Force j(x) is conservative). We assume that**

∇ _· j(x) = 0._ (9)

The Fokker-Planck equation (FP) typically models a physical system which exchanges energy with an
external environment (Ottinger, 2005; Qian, 2014). In our case, this physical system is the gradient
dynamics ∇ _· (∇_ _f ρ) while the interaction with the environment is through the term involving_
temperature: β _[−][1]∇_ _· (∇_ _·_ (Dρ)). The second law of thermodynamics states that the entropy of a
system can never decrease; in Appendix B we show how the above assumption is sufficient to satisfy
the second law. We also discuss some properties of j(x) in Appendix C that are a consequence of
this. The most important is that j(x) is always orthogonal to ∇ρ [ss]. We illustrate the effects of this
assumption in Example 19.

This leads us to the main result of this section.

**Theorem 5 (SGD performs variational inference). The functional**

_F(ρ) = β_ _[−][1]_ KL�ρ || ρ [ss][�] (10)

_decreases monotonically along the trajectories of the Fokker-Planck equation (FP) and converges to_
_its minimum, which is zero, at steady-state. Moreover, we also have an energetic-entropic split_

_F(ρ) = E x∈ρ_ �Φ(x)� _−_ _β_ _[−][1]H(ρ)+_ constant. (11)

Theorem 5, proven in Appendix F.1, shows that SGD implicitly minimizes a combination of two terms:
an “energetic” term, and an “entropic” term. The first is the average potential over a distribution ρ.
The steady-state of SGD in (6) is such that it places most of its probability mass in regions of the
parameter space with small values of Φ. The second shows that SGD has an implicit bias towards
solutions that maximize the entropy of the distribution ρ.

Note that the energetic term in (11) has potential Φ(x), instead of f (x). This is an important fact and
the crux of this paper.


-----

**Lemma 6 (Potential equals original loss iff isotropic diffusion). If the diffusion matrix D(x) is**
_isotropic, i.e., a constant multiple of the identity, the implicit potential is the original loss itself_

_D(x) = c Id×d_ _⇔_ Φ(x) = f (x). (12)

This is proven in Appendix F.2. The definition in (8) shows that j ̸= 0 when D(x) is non-isotropic.
This results in a deterministic component in the SGD dynamics which does not affect the functional
_F(ρ), hence j(x) is called a “conservative force.” The following lemma is proven in Appendix F.3._

**Lemma 7 (Most likely trajectories of SGD are limit cycles). The force j(x) does not decrease**
_F(ρ) in (11) and introduces a deterministic component in SGD given by_

_x˙ = j(x)._ (13)

_The condition ∇_ _· j(x) = 0 in Assumption 4 implies that most likely trajectories of SGD traverse_
_closed trajectories in weight space._

3.1 WASSERSTEIN GRADIENT FLOW

Theorem 5 applies for a general D(x) and it is equivalent to the celebrated JKO functional (Jordan
et al., 1997) in optimal transportation (Santambrogio, 2015; Villani, 2008) if the diffusion matrix is
isotropic. Appendix D provides a brief overview using the heat equation as an example.

**Corollary 8 (Wasserstein gradient flow for isotropic noise). If D(x) = I, trajectories of the Fokker-**
_Planck equation (FP) are gradient flow in the Wasserstein metric of the functional_

_F(ρ) = E x∼ρ_ � _f_ (x)� _−_ _β_ _[−][1]H(ρ)._ (JKO)

Observe that the energetic term contains f (x) in Corollary 8. The proof follows from Theorem 5
and Lemma 6, see Santambrogio (2017) for a rigorous treatment of Wasserstein metrics. The JKO
functional above has had an enormous impact in optimal transport because results like Theorem 5
and Corollary 8 provide a way to modify the functional F(ρ) in an interpretable fashion. Modifying
the Fokker-Planck equation or the SGD updates directly to enforce regularization properties on the
solutions ρ [ss] is much harder.

3.2 CONNECTION TO BAYESIAN INFERENCE

Note the absence of any prior in (11). On the other hand, the evidence lower bound (Kingma and
Welling, 2013) for the dataset Ξ is,

_−_ log p(Ξ) ≤ E x∼q� _f_ (x)� + KL�q(x _|_ Ξ) || p(x _|_ Ξ)�,

(ELBO)
_≤_ E x∼q� _f_ (x)� _−_ _H(q)+_ _H(q, p);_

where H(q, p) is the cross-entropy of the estimated steady-state and the variational prior. The implicit
loss function of SGD in (11) therefore corresponds to a uniform prior p(x _|_ Ξ). In other words, we
have shown that SGD itself performs variational optimization with a uniform prior. Note that this
prior is well-defined by our hypothesis of x ∈ Ω for some compact Ω.

It is important to note that SGD implicitly minimizes a potential Φ(x) instead of the original loss
_f_ (x) in ELBO. We prove in Section 5 that this potential is quite different from f (x) if the diffusion
matrix D is non-isotropic, in particular, with respect to its critical points.

**Remark 9 (SGD has an information bottleneck). The functional (11) is equivalent to the informa-**
tion bottleneck principle in representation learning (Tishby et al., 1999). Minimizing this functional,
explicitly, has been shown to lead to invariant representations (Achille and Soatto, 2017). Theorem 5
shows that SGD implicitly contains this bottleneck and therefore begets these properties, naturally.

**Remark 10 (ELBO prior conflicts with SGD). Working with ELBO in practice involves one or**
multiple steps of SGD to minimize the energetic term along with an estimate of the KL-divergence


-----

term, often using a factored Gaussian prior (Kingma and Welling, 2013; Jordan et al., 1999). As Theorem 5 shows, such an approach also enforces a uniform prior whose strength is determined by β _[−][1]_

and conflicts with the externally imposed Gaussian prior. This conflict—which fundamentally arises
from using SGD to minimize the energetic term—has resulted in researchers artificially modulating
the strength of the KL-divergence term using a scalar pre-factor (Mandt et al., 2016).

3.3 PRACTICAL IMPLICATIONS

We will show in Section 5 that the potential Φ(x) does not depend on the optimization process, it
is only a function of the dataset and the architecture. The effect of two important parameters, the
learning rate η and the mini-batch size b therefore completely determines the strength of the entropic
regularization term. If β _[−][1]_ _→_ 0, the implicit regularization of SGD goes to zero. This implies that

_β_ _[−][1]_ = _[η]_

2b [should not be small]

is a good tenet for regularization of SGD.

**Remark 11 (Learning rate should scale linearly with batch-size to generalize well). In order to**
maintain the entropic regularization, the learning rate η needs to scale linearly with the batch-size
_b. This prediction, based on Theorem 5, fits very well with empirical evidence wherein one obtains_
good generalization performance only with small mini-batches in deep networks (Keskar et al., 2016),
or via such linear scaling (Goyal et al., 2017).

**Remark 12 (Sampling with replacement is better than without replacement). The diffusion**
matrix for the case when mini-batches are sampled with replacement is very close to (2), see Appendix A.2. However, the corresponding inverse temperature is


�
should not be small.


_β_ _[′−][1]_ = _[η]_

2b


�
1 _−_ _[b]_

_N_


The extra factor of �1 _−_ _N[b]_ � reduces the entropic regularization in (11), as b → _N, the inverse_

temperature β _[′]_ _→_ ∞. As a consequence, for the same learning rate η and batch-size b, Theorem 5
predicts that sampling with replacement has better regularization than sampling without replacement.
This effect is particularly pronounced at large batch-sizes.

### 4 EMPIRICAL CHARACTERIZATION OF SGD DYNAMICS

Section 4.1 shows that the diffusion matrix D(x) for modern deep networks is highly non-isotropic
with a very low rank. We also analyze trajectories of SGD and detect periodic components using a
frequency analysis in Section 4.2; this validates the prediction of Lemma 7.

We consider three networks for these experiments: a convolutional network called small-lenet, a twolayer fully-connected network on MNIST (LeCun et al., 1998) and a smaller version of the All-CNN-C
architecture of Springenberg et al. (2014) on the CIFAR-10 and CIFAR-100 datasets (Krizhevsky,
2009); see Appendix E for more details.

4.1 HIGHLY NON-ISOTROPIC D(x) FOR DEEP NETWORKS

Figs. 1 and 2 show the eigenspectrum[1] of the diffusion matrix. In all cases, it has a large fraction of
almost-zero eigenvalues with a very small rank that ranges between 0.3% - 2%. Moreover, non-zero
eigenvalues are spread across a vast range with a large variance.

**Remark 13 (Noise in SGD is largely independent of the weights). The variance of noise in (3) is**


_η D(xk)_ = 2 β _[−][1]D(xk)._

_b_

1thresholded at λmax × _d ×_ [machine-precision. This formula is widely used, for instance, in numpy.](https://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.linalg.matrix_rank.html)


-----

4
10

2
10


0
10

5 3 1 1
10 10 10 10


(a) MNIST: small-lenet (b) MNIST: small-fc
_λ_ (D) = (0.3 ± 2.11) _×_ 10[−][3] _λ_ (D) = (0.9 ± 18.5) _×_ 10[−][3]

rank(D) = 1.8% rank(D) = 0.6%

Figure 1: Eigenspectrum of D(x) at three instants during training (20%, 40% and 100% completion, darker
is later). The eigenspectrum in Fig. 1b for the fully-connected network has a much smaller rank and much
larger variance than the one in Fig. 1a which also performs better on MNIST. This indicates that convolutional
networks are better conditioned than fully-connected networks in terms of D(x).


We have plotted the eigenspectra of the diffusion matrix in Fig. 1 and Fig. 2 at three different
instants, 20%, 40% and 100% training completion; they are almost indistinguishable. This implies
that the variance of the mini-batch gradients in deep networks can be considered a constant, highly
non-isotropic matrix.

**Remark 14 (More non-isotropic diffusion if data is diverse). The eigenspectra in Fig. 2 for**
CIFAR-10 and CIFAR-100 have much larger eigenvalues and standard-deviation than those in Fig. 1,
this is expected because the images in the CIFAR datasets have more variety than those in MNIST.
Similarly, while CIFAR-100 has qualitatively similar images as CIFAR-10, it has 10× more classes
and as a result, it is a much harder dataset. This correlates well with the fact that both the mean
and standard-deviation of the eigenvalues in Fig. 2b are much higher than those in Fig. 2a. Input
augmentation increases the diversity of mini-batch gradients. This is seen in Fig. 2c where the
standard-deviation of the eigenvalues is much higher as compared to Fig. 2a.


4
10

2
10


0
10

2 0 2
10 10 10

eigenvalues


2 0 2
10 10 10

eigenvalues


2 0 2
10 10 10

eigenvalues

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||MN = ( ran m tru one itio eig d 1 e m on -10 se R- m n o es the||10 e IS 0.3 k(D of m i in ne en 00 in -is 0 the 100 uc f t the ei||3 ige T: s ± ) D(x n F Fig d th spe % i-b otr hav im h h h he di gen||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||1 nva sm 18 = 0 an a m his ). nd ist on e e dev ari -10 th tha s s g.||1 0 lue all .5) .6% d uc in Fi ing sid ige iat et, i e f n ee 2a.|s -fc ×1 100 h s dica g. uis ere ns ion y th t ha act tho n in|||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||


(a) CIFAR-10
_λ_ (D) = 0.27 ± 0.84
rank(D) = 0.34%


(b) CIFAR-100
_λ_ (D) = 0.98 ± 2.16
rank(D) = 0.47%


(c) CIFAR-10: data augmentation
_λ_ (D) = 0.43 ± 1.32
rank(D) = 0.32%


Figure 2: Eigenspectrum of D(x) at three instants during training (20%, 40% and 100% completion, darker is
later). The eigenvalues are much larger in magnitude here than those of MNIST in Fig. 1, this suggests a larger
gradient diversity for CIFAR-10 and CIFAR-100. The diffusion matrix for CIFAR-100 in Fig. 2b has larger
eigenvalues and is more non-isotropic and has a much larger rank than that of Fig. 2a; this suggests that gradient
diversity increases with the number of classes. As Fig. 2a and Fig. 2c show, augmenting input data increases
both the mean and the variance of the eigenvalues while keeping the rank almost constant.

**Remark 15 (Inverse temperature scales with the mean of the eigenspectrum). Remark 14 shows**
that the mean of the eigenspectrum is large if the dataset is diverse. Based on this, we propose that


-----

the inverse temperature β should scale linearly with the mean of the eigenvalues of D:


_d_ �
## ∑ λ (D)
_k=1_


� _η_

_b_


� [�] 1
_d_


= constant; (14)


where d is the number of weights. This keeps the noise in SGD constant in magnitude for different
values of the learning rate η, mini-batch size b, architectures, and datasets. Note that other hyperparameters which affect stochasticity such as dropout probability are implicit inside D.

**Remark 16 (Variance of the eigenspectrum informs architecture search). Compare the eigen-**
spectra in Figs. 1a and 1b with those in Figs. 2a and 2c. The former pair shows that small-lenet which
is a much better network than small-fc also has a much larger rank, i.e., the number of non-zero
eigenvalues (D(x) is symmetric). The second pair shows that for the same dataset, data-augmentation
creates a larger variance in the eigenspectrum. This suggests that both the quantities, viz., rank
of the diffusion matrix and the variance of the eigenspectrum, inform the performance of a given
architecture on the dataset. Note that as discussed in Remark 15, the mean of the eigenvalues can be
controlled using the learning rate η and the batch-size b.

This observation is useful for automated architecture search where we can use the quantity


rank(D)

+ var (λ (D))
_d_

to estimate the efficacy of a given architecture, possibly, without even training, since D does not
depend on the weights much. This task currently requires enormous amounts of computational
power (Zoph and Le, 2016; Baker et al., 2016; Brock et al., 2017).


0.003

0.002


0.001 1 3 5

10 10 10

epochs


0.00 5 4 3 2

10 10 10 10

frequency (1/epoch)


0.2 3 4 5

10 10 10

lag (epochs)

|0.15|Col2|Col3|Col4|
|---|---|---|---|
|0.15 0.10 amplitude 0.05 0.00||||
|||||
|||||

|1.0|Col2|Col3|
|---|---|---|
|auto-correlation 0.6 0.2 0.2|||
||||
||||
||||

|Col1|Col2|
|---|---|
|||


(a) FFT of xk[i] +1 _[−]_ _[x]k[i]_


(b) Auto-correlation (AC) of xk[i]


(c) Normalized gradient _[∥][∇]√[f]_ [(][x][k][)][∥]

_d_


Figure 3: Fig. 3a shows the Fast Fourier Transform (FFT) of xk[i] +1 _[−]_ _[x]k[i]_ [where][ k][ is the number of epochs and][ i]
denotes the index of the weight. Fig. 3b shows the auto-correlation of xk[i] [with][ 99%][ confidence bands denoted by]
the dotted red lines. Both Figs. 3a and 3b show the mean and one standard-deviation over the weight index i; the
standard deviation is very small which indicates that all the weights have a very similar frequency spectrum.
Figs. 3a and 3b should be compared with the FFT of white noise which should be flat and the auto-correlation of
Brownian motion which quickly decays to zero, respectively. Figs. 3 and 3a therefore show that trajectories of
SGD are not simply Brownian motion. Moreover the gradient at these locations is quite large (Fig. 3c).

4.2 ANALYSIS OF LONG-TERM TRAJECTORIES


We train a smaller version of small-fc on 7 _×_ 7 down-sampled MNIST images for 10[5] epochs and
store snapshots of the weights after each epoch to get a long trajectory in the weight space. We
discard the first 10[3] epochs of training (“burnin”) to ensure that SGD has reached the steady-state.
The learning rate is fixed to 10[−][3] after this, up to 10[5] epochs.

**Remark 17 (Low-frequency periodic components in SGD trajectories). Iterates of SGD, after**
it reaches the neighborhood of a critical point ∥∇ _f_ (xk)∥≤ _ε, are expected to perform Brownian_
motion with variance var (∇ _fb(x)), the FFT in Fig. 3a would be flat if this were so. Instead, we_
see low-frequency modes in the trajectory that are indicators of a periodic dynamics of the force
_j(x). These modes are not sharp peaks in the FFT because j(x) can be a non-linear function of the_


-----

weights thereby causing the modes to spread into all dimensions of x. The FFT is dominated by
jittery high-frequency modes on the right with a slight increasing trend; this suggests the presence of
colored noise in SGD at high-frequencies.

The auto-correlation (AC) in Fig. 3b should be compared with the AC for Brownian motion which
decays to zero very quickly and stays within the red confidence bands (99%). Our iterates are
significantly correlated with each other even at very large lags. This further indicates that trajectories
of SGD do not perform Brownian motion.
**Remark 18 (Gradient magnitude in deep networks is always large). Fig. 3c shows that the full-**
gradient computed over the entire dataset (without burnin) does not decrease much with respect to
the number of epochs. While it is expected to have a non-zero gradient norm because SGD only
converges to a neighborhood of a critical point for non-zero learning rates, the magnitude of this
gradient norm is quite large. This magnitude drops only by about a factor of 3 over the next 10[5]

epochs. The presence of a non-zero j(x) also explains this, it causes SGD to be away from critical
points, this phenomenon is made precise in Theorem 22. Let us note that a similar plot is also seen
in Shwartz-Ziv and Tishby (2017) for the per-layer gradient magnitude.

### 5 SGD FOR DEEP NETWORKS IS OUT-OF-EQUILIBRIUM

This section now gives an explicit formula for the potential Φ(x). We also discuss implications of
this for generalization in Section 5.3.

The fundamental difficulty in obtaining an explicit expression for Φ is that even if the diffusion matrix
_D(x) is full-rank, there need not exist a function Φ(x) such that ∇Φ(x) = D[−][1](x) ∇_ _f_ (x) at all x ∈ Ω.
We therefore split the analysis into two cases:

(i) a local analysis near any critical point ∇ _f_ (x) = 0 where we linearize ∇ _f_ (x) = Fx and ∇Φ(x) =
_Ux to compute U = G[−][1]_ _F for some G, and_
(ii) the general case where ∇Φ(x) cannot be written as a local rotation and scaling of ∇ _f_ (x).

Let us introduce these cases with an example from Noh and Lee (2015).


1

0

1


1

0

1


1 0 1


1 0 1

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||


(a) λ = 0


(b) λ = 0.5


(c) λ = 1.5


Figure 4: Gradient field for the dynamics in Example 19: line-width is proportional to the magnitude of
the gradient ∥∇ _f_ (x)∥, red dots denote the most likely locations of the steady-state e[−][Φ] while the potential
Φ is plotted as a contour map. The critical points of f (x) and Φ(x) are the same in Fig. 4a, namely (±1, 0),
because the force j(x) = 0. For λ = 0.5 in Fig. 4b, locations where ∇ _f_ (x) = 0 have shifted slightly as predicted
by Theorem 22. The force field also has a distinctive rotation component, see Remark 21. In Fig. 4c with a
large ∥ _j(x)∥, SGD converges to limit cycles around the saddle point at the origin. This is highly surprising and_
demonstrates that the solutions obtained by SGD may be very different from local minima.

**Example 19 (Double-well potential with limit cycles). Define**

1 _[−]_ [1][)][2] 2
Φ(x) = [(][x][2] 4 + _[x]2[2]_ _[.]_

Instead of constructing a diffusion matrix D(x), we will directly construct different gradients ∇ _f_ (x)
that lead to the same potential Φ; these are equivalent but the later is much easier. The dynamics is


-----

_√_
given by dx = −∇ _f_ (x) dt + 2 dW (t), where ∇ _f_ (x) = − _j(x)+_ ∇Φ(x). We pick j = λ _e[Φ]_ _J[ss](x) for_

some parameter λ > 0 where

(x1[2][+][x]2[2][)][2]
_J[ss](x) = e[−]_ 4 (−x2, x1).

Note that this satisfies (6) and does not change ρ [ss] = e[−][Φ]. Fig. 4 shows the gradient field f (x) along
with a discussion.

5.1 LINEARIZATION AROUND A CRITICAL POINT

Without loss of generality, let x = 0 be a critical point of f (x). This critical point can be a local
minimum, maximum, or even a saddle point. We linearize the gradient around the origin and define
a fixed matrix F ∈ R[d][×][d] (the Hessian) to be ∇ _f_ (x) = Fx. Let D = D(0) be the constant diffusion
matrix matrix. The dynamics in (3) can now be written as


_dx = −Fx dt +_ �


2β _[−][1]_ _D dW_ (t). (15)


**Lemma 20 (Linearization). The matrix F in (15) can be uniquely decomposed into**

_F = (D_ + _Q) U;_ (16)

_D and Q are the symmetric and anti-symmetric parts of a matrix G with GF_ _[⊤]_ _−_ _FG[⊤]_ = 0, to get
Φ(x) = [1]2 _[x][⊤][Ux.]_

The above lemma is a classical result if the critical point is a local minimum, i.e., if the loss is locally
convex near x = 0; this case has also been explored in machine learning before (Mandt et al., 2016).
We refer to Kwon et al. (2005) for the proof that linearizes around any critical point.

**Remark 21 (Rotation of gradients). We see from Lemma 20 that, near a critical point,**

∇ _f = (D_ + _Q) ∇Φ_ _−_ _β_ _[−][1]∇_ _·_ _D_ _−_ _β_ _[−][1]∇_ _·_ _Q_ (17)

up to the first order. This suggests that the effect of j(x) is to rotate the gradient field and move the
critical points, also seen in Fig. 4b. Note that ∇ _·_ _D = 0 and ∇_ _·_ _Q = 0 in the linearized analysis._

5.2 GENERAL CASE

We next give the general expression for the deviation of the critical points ∇Φ from those of the
original loss ∇ _f_ .

**A-type stochastic integration:** A Fokker-Planck equation is a deterministic partial differential
equation (PDE) and every steady-state distribution, ρ [ss] ∝ _e[−][β]_ [Φ] in this case, has a unique such PDE
that achieves it. However, the same PDE can be tied to different SDEs depending on the stochastic
integration scheme, e.g., Ito, Stratonovich (Risken, 1996; Oksendal, 2003), Hanggi (Hanggi¨, 1978),
_α-type etc. An “A-type” interpretation is one such scheme (Ao et al., 2007; Shi et al., 2012). It is_
widely used in non-equilibrium studies in physics and biology (Wang et al., 2008; Zhu et al., 2004)
because it allows one to compute the steady-state distribution easily; its implications are supported
by other mathematical analyses such as Tel et al. (1989); Qian (2014).

The main result of the section now follows. It exploits the A-type interpretation to compute the
difference between the most likely locations of SGD which are given by the critical points of the
potential Φ(x) and those of the original loss f (x).

**Theorem 22 (Most likely locations are not the critical points of the loss). The Ito SDE**


�
_dx = −∇_ _f_ (x) dt +


2β _[−][1]D(x) dW_ (t)


_is equivalent to the A-type SDE (Ao et al., 2007; Shi et al., 2012)_

_dx = −�D(x)+_ _Q(x)�_ ∇Φ(x) dt + �2β _[−][1]D(x) dW_ (t) (18)


-----

_with the same steady-state distribution ρ_ [ss] ∝ _e[−][β]_ [Φ][(][x][)] _and Fokker-Planck equation (FP) if_

∇ _f_ (x) = �D(x)+ _Q(x)�_ ∇Φ(x) _−_ _β_ _[−][1]∇_ _·_ �D(x)+ _Q(x)�._ (19)

_The anti-symmetric matrix Q(x) and the potential Φ(x) can be explicitly computed in terms of the_
_gradient ∇_ _f_ (x) and the diffusion matrix D(x). The potential Φ(x) does not depend on β _._

See Appendix F.4 for the proof. It exploits the fact that the the Ito SDE (3) and the A-type SDE (18)
should have the same Fokker-Planck equations because they have the same steady-state distributions.

**Remark 23 (SGD is far away from critical points). The time spent by a Markov chain at a state x is**
proportional to its steady-state distribution ρ [ss](x). While it is easily seen that SGD does not converge
in the Cauchy sense due to the stochasticity, it is very surprising that it may spend a significant amount
of time away from the critical points of the original loss. If D(x)+ _Q(x) has a large divergence, the_
set of states with ∇Φ(x) = 0 might be drastically different than those with ∇ _f_ (x) = 0. This is also
seen in example Fig. 4c; in fact, SGD may even converge around a saddle point.

This also closes the logical loop we began in Section 3 where we assumed the existence of ρ [ss] and
defined the potential Φ using it. Lemma 20 and Theorem 22 show that both can be defined uniquely
in terms of the original quantities, i.e., the gradient term ∇ _f_ (x) and the diffusion matrix D(x). There
is no ambiguity as to whether the potential Φ(x) results in the steady-state ρ [ss](x) or vice-versa.

**Remark 24 (Consistent with the linear case). Theorem 22 presents a picture that is completely**
consistent with Lemma 20. If j(x) = 0 and Q(x) = 0, or if Q is a constant like the linear case
in Lemma 20, the divergence of Q(x) in (19) is zero.

**Remark 25 (Out-of-equilibrium effect can be large even if D is constant). The presence of a**
_Q(x) with non-zero divergence is the consequence of a non-isotropic D(x) and it persists even if D is_
constant and independent of weights x. So long as D is not isotropic, as we discussed in the beginning
of Section 5, there need not exist a function Φ(x) such that ∇Φ(x) = D[−][1] ∇ _f_ (x) at all x. This is also
seen in our experiments, the diffusion matrix is almost constant with respect to weights for deep
networks, but consequences of out-of-equilibrium behavior are still seen in Section 4.2.

**Remark 26 (Out-of-equilibrium effect increases with β** _[−][1]). The effect predicted by (19) becomes_
more pronounced if β _[−][1]_ = 2[η]b [is large. In other words, small batch-sizes or high learning rates]

cause SGD to be drastically out-of-equilibrium. Theorem 5 also shows that as β _[−][1]_ _→_ 0, the implicit
entropic regularization in SGD vanishes. Observe that these are exactly the conditions under which we
typically obtain good generalization performance for deep networks (Keskar et al., 2016; Goyal et al.,
2017). This suggests that non-equilibrium behavior in SGD is crucial to obtain good generalization
performance, especially for high-dimensional models such as deep networks where such effects are
expected to be more pronounced.

5.3 GENERALIZATION

It was found that solutions of discrete learning problems that generalize well belong to dense clusters
in the weight space (Baldassi et al., 2015; 2016). Such dense clusters are exponentially fewer
compared to isolated solutions. To exploit these observations, the authors proposed a loss called
“local entropy” that is out-of-equilibrium by construction and can find these well-generalizable
solutions easily. This idea has also been successful in deep learning where Chaudhari et al. (2016)
modified SGD to seek solutions in “wide minima” with low curvature to obtain improvements in
generalization performance as well as convergence rate (Chaudhari et al., 2017a).

Local entropy is a smoothed version of the original loss given by

�
_fγ_ (x) = − log _Gγ ∗_ _e[−]_ _[f]_ [(][x][)][�] _,_

where Gγ is a Gaussian kernel of variance γ. Even with an isotropic diffusion matrix, the steady-state
distribution with fγ (x) as the loss function is ργ[ss][(][x][)][ ∝] _[e][−][β][ f][γ]_ [(][x][)][. For large values of][ γ][, the new loss]
makes the original local minima exponentially less likely. In other words, local entropy does not
rely on non-isotropic gradient noise to obtain out-of-equilibrium behavior, it gets it explicitly, by


-----

construction. This is also seen in Fig. 4c: if SGD is drastically out-of-equilibrium, it converges
around the “wide” saddle point region at the origin which has a small local entropy.

Actively constructing out-of-equilibrium behavior leads to good generalization in practice. Our
evidence that SGD on deep networks itself possesses out-of-equilibrium behavior then indicates that
SGD for deep networks generalizes well because of such behavior.

### 6 RELATED WORK

**SGD, variational inference and implicit regularization:** The idea that SGD is related to variational inference has been seen in machine learning before (Duvenaud et al., 2016; Mandt et al., 2016)
under assumptions such as quadratic steady-states; for instance, see Mandt et al. (2017) for methods
to approximate steady-states using SGD. Our results here are very different, we would instead like to
understand properties of SGD itself. Indeed, in full generality, SGD performs variational inference
using a new potential Φ that it implicitly constructs given an architecture and a dataset.

It is widely believed that SGD is an implicit regularizer, see Zhang et al. (2016); Neyshabur et al.
(2017); Shwartz-Ziv and Tishby (2017) among others. This belief stems from its remarkable empirical
performance. Our results show that such intuition is very well-placed. Thanks to the special
architecture of deep networks where gradient noise is highly non-isotropic, SGD helps itself to a
potential Φ with properties that lead to both generalization and acceleration.

**SGD and noise:** Noise is often added in SGD to improve its behavior around saddle points for
non-convex losses, see Lee et al. (2016); Anandkumar and Ge (2016); Ge et al. (2015). It is also
quite indispensable for training deep networks (Hinton and Van Camp, 1993; Srivastava et al., 2014;
Kingma et al., 2015; Gulcehre et al., 2016; Achille and Soatto, 2017). There is however a disconnect
between these two directions due to the fact that while adding external gradient noise helps in theory,
it works poorly in practice (Neelakantan et al., 2015; Chaudhari and Soatto, 2015). Instead, “noise
tied to the architecture” works better, e.g., dropout, or small mini-batches. Our results close this gap
and show that SGD crucially leverages the highly degenerate noise induced by the architecture.

**Gradient diversity:** Yin et al. (2017) construct a scalar measure of the gradient diversity given by
∑k∥∇ _fk(x)∥/∥∇_ _f_ (x)∥, and analyze its effect on the maximum allowed batch-size in the context of
distributed optimization.

**Markov Chain Monte Carlo:** MCMC methods that sample from a negative log-likelihood Φ(x)
have employed the idea of designing a force j = ∇Φ _−_ ∇ _f to accelerate convergence, see Ma et al._
(2015) for a thorough survey, or Pavliotis (2016); Kaiser et al. (2017) for a rigorous treatment. We
instead compute the potential Φ given ∇ _f and D, which necessitates the use of techniques from_
physics. In fact, our results show that since j ̸= 0 for deep networks due to non-isotropic gradient
noise, very simple algorithms such as SGLD by Welling and Teh (2011) also benefit from the
acceleration that their sophisticated counterparts aim for (Ding et al., 2014; Chen et al., 2016).

### 7 DISCUSSION

The continuous-time point-of-view used in this paper gives access to general principles that govern
SGD, such analyses are increasingly becoming popular (Wibisono et al., 2016; Chaudhari et al.,
2017b). However, in practice, deep networks are trained for only a few epochs with discrete-time
updates. Closing this gap is an important future direction. A promising avenue towards this is that for
typical conditions in practice such as small mini-batches or large learning rates, SGD converges to
the steady-state distribution quickly (Raginsky et al., 2017).


-----

### 8 ACKNOWLEDGMENTS

PC would like to thank Adam Oberman for introducing him to the JKO functional. The authors
would also like to thank Alhussein Fawzi for numerous discussions during the conception of this
paper and his contribution to its improvement.

### REFERENCES

Achille, A. and Soatto, S. (2017). On the emergence of invariance and disentangling in deep representations.
_arXiv:1706.01350._

Anandkumar, A. and Ge, R. (2016). Efficient approaches for escaping higher order saddle points in non-convex
optimization. In COLT, pages 81–102.

Ao, P., Kwon, C., and Qian, H. (2007). On the existence of potential landscape in the evolution of complex
systems. Complexity, 12(4):19–27.

Baker, B., Gupta, O., Naik, N., and Raskar, R. (2016). Designing neural network architectures using reinforcement learning. arXiv:1611.02167.

Baldassi, C., Borgs, C., Chayes, J., Ingrosso, A., Lucibello, C., Saglietti, L., and Zecchina, R. (2016). Unreasonable effectiveness of learning neural networks: From accessible states and robust ensembles to basic
algorithmic schemes. PNAS, 113(48):E7655–E7662.

Baldassi, C., Ingrosso, A., Lucibello, C., Saglietti, L., and Zecchina, R. (2015). Subdominant dense clusters
allow for simple learning and high computational performance in neural networks with discrete synapses.
_Physical review letters, 115(12):128101._

Brock, A., Lim, T., Ritchie, J., and Weston, N. (2017). SMASH: One-Shot Model Architecture Search through
HyperNetworks. arXiv:1708.05344.

Chaudhari, P., Baldassi, C., Zecchina, R., Soatto, S., Talwalkar, A., and Oberman, A. (2017a). Parle: parallelizing
stochastic gradient descent. arXiv:1707.00424.

Chaudhari, P., Choromanska, A., Soatto, S., LeCun, Y., Baldassi, C., Borgs, C., Chayes, J., Sagun, L., and
Zecchina, R. (2016). Entropy-SGD: biasing gradient descent into wide valleys. arXiv:1611.01838.

Chaudhari, P., Oberman, A., Osher, S., Soatto, S., and Guillame, C. (2017b). Deep Relaxation: partial differential
equations for optimizing deep neural networks. arXiv:1704.04932.

Chaudhari, P. and Soatto, S. (2015). On the energy landscape of deep networks. arXiv:1511.06485.

Chen, C., Carlson, D., Gan, Z., Li, C., and Carin, L. (2016). Bridging the gap between stochastic gradient
MCMC and stochastic optimization. In AISTATS, pages 1051–1060.

Ding, N., Fang, Y., Babbush, R., Chen, C., Skeel, R., and Neven, H. (2014). Bayesian sampling using stochastic
gradient thermostats. In NIPS, pages 3203–3211.

Duvenaud, D., Maclaurin, D., and Adams, R. (2016). Early stopping as non-parametric variational inference. In
_AISTATS, pages 1070–1077._

Frank, T. D. (2005). Nonlinear Fokker-Planck equations: fundamentals and applications. Springer Science &
Business Media.

Ge, R., Huang, F., Jin, C., and Yuan, Y. (2015). Escaping from saddle points online stochastic gradient for
tensor decomposition. In COLT, pages 797–842.

Goyal, P., Dollr, P., Girshick, R., Noordhuis, P., Wesolowski, L., Kyrola, A., Tulloch, A., Jia, Y., and He, K.
(2017). Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour. arXiv:1706.02677.

Gulcehre, C., Moczulski, M., Denil, M., and Bengio, Y. (2016). Noisy activation functions. In ICML, pages
3059–3068.

Hanggi, P. (1978). On derivations and solutions of master equations and asymptotic representations.¨ _Zeitschrift_
_f¨ur Physik B Condensed Matter, 30(1):85–95._

Hinton, G. E. and Van Camp, D. (1993). Keeping the neural networks simple by minimizing the description
length of the weights. In Proceedings of the sixth annual conference on Computational learning theory, pages
5–13. ACM.

Jaynes, E. T. (1980). The minimum entropy production principle. Annual Review of Physical Chemistry,
31(1):579–601.


-----

Jordan, M. I., Ghahramani, Z., Jaakkola, T. S., and Saul, L. K. (1999). An introduction to variational methods
for graphical models. Machine learning, 37(2):183–233.

Jordan, R., Kinderlehrer, D., and Otto, F. (1997). Free energy and the fokker-planck equation. Physica D:
_Nonlinear Phenomena, 107(2-4):265–271._

Jordan, R., Kinderlehrer, D., and Otto, F. (1998). The variational formulation of the Fokker–Planck equation.
_SIAM journal on mathematical analysis, 29(1):1–17._

Kaiser, M., Jack, R. L., and Zimmer, J. (2017). Acceleration of convergence to equilibrium in Markov chains by
breaking detailed balance. Journal of Statistical Physics, 168(2):259–287.

Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., and Tang, P. T. P. (2016). On large-batch training for
deep learning: Generalization gap and sharp minima. arXiv:1609.04836.

Kingma, D. P., Salimans, T., and Welling, M. (2015). Variational dropout and the local reparameterization trick.
In NIPS, pages 2575–2583.

Kingma, D. P. and Welling, M. (2013). Auto-encoding variational Bayes. arXiv:1312.6114.

Krizhevsky, A. (2009). Learning multiple layers of features from tiny images. Master’s thesis, Computer Science,
University of Toronto.

Kwon, C., Ao, P., and Thouless, D. J. (2005). Structure of stochastic dynamics near fixed points. Proceedings of
_the National Academy of Sciences of the United States of America, 102(37):13029–13033._

LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. (1998). Gradient-based learning applied to document
recognition. Proceedings of the IEEE, 86(11):2278–2324.

Lee, J. D., Simchowitz, M., Jordan, M. I., and Recht, B. (2016). Gradient descent only converges to minimizers.
In COLT, pages 1246–1257.

Li, C. J., Li, L., Qian, J., and Liu, J.-G. (2017a). Batch size matters: A diffusion approximation framework on
nonconvex stochastic gradient descent. arXiv:1705.07562.

Li, Q., Tai, C., and Weinan, E. (2017b). Stochastic modified equations and adaptive stochastic gradient algorithms.
In ICML, pages 2101–2110.

Ma, Y.-A., Chen, T., and Fox, E. (2015). A complete recipe for stochastic gradient MCMC. In NIPS, pages
2917–2925.

Mandt, S., Hoffman, M., and Blei, D. (2016). A variational analysis of stochastic gradient algorithms. In ICML,
pages 354–363.

Mandt, S., Hoffman, M. D., and Blei, D. M. (2017). Stochastic Gradient Descent as Approximate Bayesian
Inference. arXiv:1704.04289.

Neelakantan, A., Vilnis, L., Le, Q. V., Sutskever, I., Kaiser, L., Kurach, K., and Martens, J. (2015). Adding
gradient noise improves learning for very deep networks. arXiv:1511.06807.

Neyshabur, B., Tomioka, R., Salakhutdinov, R., and Srebro, N. (2017). Geometry of optimization and implicit
regularization in deep learning. arXiv:1705.03071.

Noh, J. D. and Lee, J. (2015). On the steady-state probability distribution of nonequilibrium stochastic systems.
_Journal of the Korean Physical Society, 66(4):544–552._

Oksendal, B. (2003). Stochastic differential equations. Springer.

Onsager, L. (1931a). Reciprocal relations in irreversible processes. I. Physical review, 37(4):405.

Onsager, L. (1931b). Reciprocal relations in irreversible processes. II. Physical review, 38(12):2265.

Ottinger, H. (2005). Beyond equilibrium thermodynamics. John Wiley & Sons.

Otto, F. (2001). The geometry of dissipative evolution equations: the porous medium equation.

Pavliotis, G. A. (2016). Stochastic processes and applications. Springer.

Prigogine, I. (1955). Thermodynamics of irreversible processes, volume 404. Thomas.

Qian, H. (2014). The zeroth law of thermodynamics and volume-preserving conservative system in equilibrium
with stochastic damping. Physics Letters A, 378(7):609–616.

Raginsky, M., Rakhlin, A., and Telgarsky, M. (2017). Non-convex learning via Stochastic Gradient Langevin
Dynamics: a nonasymptotic analysis. arXiv:1702.03849.

Risken, H. (1996). The Fokker-Planck Equation. Springer.


-----

Santambrogio, F. (2015). Optimal transport for applied mathematicians. Birkuser, NY.

Santambrogio, F. (2017). Euclidean, metric, and Wasserstein gradient flows: an overview. Bulletin of Mathemat_ical Sciences, 7(1):87–154._

Shi, J., Chen, T., Yuan, R., Yuan, B., and Ao, P. (2012). Relation of a new interpretation of stochastic differential
equations to ito process. Journal of Statistical physics, 148(3):579–590.

Shwartz-Ziv, R. and Tishby, N. (2017). Opening the black box of deep neural networks via information.
_arXiv:1703.00810._

Springenberg, J., Dosovitskiy, A., Brox, T., and Riedmiller, M. (2014). Striving for simplicity: The all
convolutional net. arXiv:1412.6806.

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., and Salakhutdinov, R. (2014). Dropout: a simple way
to prevent neural networks from overfitting. JMLR, 15(1):1929–1958.

Tel, T., Graham, R., and Hu, G. (1989). Nonequilibrium potentials and their power-series expansions. Physical
_Review A, 40(7):4065._

Tishby, N., Pereira, F. C., and Bialek, W. (1999). The information bottleneck method. In Proc. of the 37-th
_Annual Allerton Conference on Communication, Control and Computing, pages 368–377._

Villani, C. (2008). Optimal transport: old and new, volume 338. Springer Science & Business Media.

Wang, J., Xu, L., and Wang, E. (2008). Potential landscape and flux framework of nonequilibrium networks:
robustness, dissipation, and coherence of biochemical oscillations. Proceedings of the National Academy of
_Sciences, 105(34):12271–12276._

Welling, M. and Teh, Y. W. (2011). Bayesian learning via stochastic gradient Langevin dynamics. In ICML,
pages 681–688.

Wibisono, A., Wilson, A. C., and Jordan, M. I. (2016). A variational perspective on accelerated methods in
optimization. PNAS, page 201614734.

Yin, D., Pananjady, A., Lam, M., Papailiopoulos, D., Ramchandran, K., and Bartlett, P. (2017). Gradient diversity
empowers distributed learning. arXiv:1706.05699.

Yin, L. and Ao, P. (2006). Existence and construction of dynamical potential in nonequilibrium processes
without detailed balance. Journal of Physics A: Mathematical and General, 39(27):8593.

Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. (2016). Understanding deep learning requires
rethinking generalization. arXiv:1611.03530.

Zhu, X.-M., Yin, L., Hood, L., and Ao, P. (2004). Calculating biological behaviors of epigenetic states in the
phage λ life cycle. Functional & integrative genomics, 4(3):188–195.

Zoph, B. and Le, Q. V. (2016). Neural architecture search with reinforcement learning. arXiv:1611.01578.


-----

### A DIFFUSION MATRIX D(x)

In this section we denote gk := ∇ _fk(x) and g := ∇_ _f_ (x) = _N[1]_ [∑]k[N]=1 _[g][k][. Although we drop the]_

dependence of gk on x to keep the notation clear, we emphasize that the diffusion matrix D depends
on the weights x.

A.1 WITH REPLACEMENT

Let i1,..., _ib be b iid random variables in {1,_ 2,..., _N}. We would like to compute_


_b_
## ∑ gi j
_j=1_


= Ei1,...,ib


_⊤[]_

_b_ �



## ∑ gi j − g
_j=1_  _[.]_


�


��
1
_b_




�

 1

_b_




_b_
## ∑ gi j − g
_j=1_


var


�
1
_b_


Note that we have that for any j ̸= k, the random vectors gi _j and gik are independent. We therefore_
have
�
covar(gi _j_ _,_ _gik_ ) = 0 = Ei _j, ik_ (gi _j −_ _g)(gik −_ _g)[⊤][�]_

We use this to obtain


_b_
## ∑ gi j
_j=1_


= [1]

_b[2]_


�
(gk − _g) (gk −_ _g)[⊤][�]_


�


_N_
## ∑
_k=1_


_b_
_j∑=1_ var(gi _j_ ) = _N[1]b_


var


�
1
_b_


= [1]

_b_


� �
∑[N]k=1 _[g][k][ g]k[⊤]_
_−_ _g g[⊤]_
_N_


_._


We will set


_D(x) =_ [1]

_N_


� _N_
## ∑ gk g[⊤]k
_k=1_


�


_−_ _g g[⊤]._ (A1)


and assimilate the factor of b[−][1] in the inverse temperature β .

A.2 WITHOUT REPLACEMENT

Let us define an indicator random variable 1i∈b that denotes if an example i was sampled in batch b.
We can show that

var(1i∈b) = _[b]_

_N_ _[−]_ _N[b][2][2][,]_


and for i ̸= j,


covar(1i∈b, **1 j∈b) = −** _N[b][2][(]([N]N[ −] −[b]1[)])_ _[.]_

Similar to Li et al. (2017a), we can now compute


_N_
## ∑ gk 1k∈b
_k=1_


= [1]

_b[2][ var]_


�


�


� _N_
## ∑ gk 1k∈b
_k=1_


var


�
1
_b_


_N_
## ∑ gi g[⊤]j [covar][(][1][i][∈][b][,] [1] [j][∈][b][)]
_i,_ _j=1, i̸=_ _j_


= [1]

_b[2]_

= [1]

_b_


_N_
_k∑=1_ _gk g[⊤]k_ [var][(][1][k][∈][b][)+][ 1]b[2]


� �
_g g[⊤]_


�
1 _−_ _[b]_

_N_


� [�] ∑[N]k=1 _[g][k][ g]k[⊤]_ � 1
_−_ 1 _−_
_N −_ 1 _N −_ 1


_._


We will again set


�
_g g[⊤]_ (A2)


1
_D(x) =_
_N −_ 1


� _N_ �
## ∑ gk g[⊤]k
_k=1_


� 1
_−_ 1 _−_
_N −_ 1


and assimilate the factor of b[−][1][ �]1 _−_ _N[b]_ � that depends on the batch-size in the inverse temperature β .


-----

### B DISCUSSION ON ASSUMPTION 4

Let F(ρ) be as defined in (11). In non-equilibrium thermodynamics, it is assumed that the local

entropy production is a product of the force −∇ � _δδρF_ � from (A8) and the probability current −J(x,t)
from (FP). This assumption in this form was first introduced by Prigogine (1955) based on the works
of Onsager (1931a;b). See Frank (2005, Sec. 4.5) for a mathematical treatment and Jaynes (1980) for
further discussion. The rate of entropy (Si) increase is given by


� � _δ_ _F_

_β_ _[−][1][ dS]dt[i]_ [=] _x∈Ω_ [∇] _δρ_

This can now be written using (A8) again as


�
_J(x,t) dx._

�⊤ � �
+ _jρ_ ∇ _[δ]_ _[F]_

_δρ_


�
_dx._


� �

_β_ _[−][1][ dS]dt[i]_ [=] _ρ D :_ ∇ _[δ]δρ[F]_


��
∇ _[δ]_ _[F]_

_δρ_


The first term in the above expression is non-negative, in order to ensure that _[dS]dt[i]_ _[≥]_ [0, we require]


� �
0 = _jρ_ ∇ _[δ]_ _[F]_

_δρ_


�
_dx_


� � _δ_ _F_
= ∇ _·_ ( _jρ)_

_δρ_


�
_dx;_


where the second equality again follows by integration by parts. It can be shown (Frank, 2005, Sec.
4.5.5) that the condition in Assumption 4, viz., ∇ _· j(x) = 0, is sufficient to make the above integral_
vanish and therefore for the entropy generation to be non-negative.

### C SOME PROPERTIES OF THE FORCE j

The Fokker-Planck equation (FP) can be written in terms of the probability current as

0 = ρt[ss] [=][ ∇] _[·]_ �− _j ρ_ [ss] + _D ∇Φ ρ_ [ss] _−_ _β_ _[−][1](∇_ _·_ _D) ρ_ [ss] + _β_ _[−][1]∇_ _·_ (Dρ [ss])�

= ∇ _· J[ss]._

Since we have ρ [ss] ∝ _e[−][β]_ [Φ][(][x][)], from the observation (7), we also have that

0 = ρt[ss] [=][ ∇] _[·]_ �D ∇Φ ρ [ss] + _β_ _[−][1]D ∇ρ_ [ss][�] _,_

and consequently,
0 = ∇ _·_ ( _j ρ_ [ss])

(A3)

_⇒_ _j(x) =_ _[J][ss]_

_ρ_ [ss][ .]

In other words, the conservative force is non-zero only if detailed balance is broken, i.e., J[ss] _̸= 0. We_
also have

0 = ∇ _·_ ( _j ρ_ [ss])
= ρ [ss] (∇ _· j −_ _j ·_ ∇Φ) _,_

which shows using Assumption 4 and ρ [ss](x) > 0 for all x ∈ Ω that j(x) is always orthogonal to the
gradient of the potential
0 = j(x) _·_ ∇Φ(x)
(A4)
= j(x) _·_ ∇ρ [ss].

Using the definition of j(x) in (8), we have detailed balance when

∇ _f_ (x) = D(x) ∇Φ(x) _−_ _β_ _[−][1]∇_ _·_ _D(x)._ (A5)


-----

### D HEAT EQUATION AS A GRADIENT FLOW

As first discovered in the works of Jordan, Kinderleherer and Otto (Jordan et al., 1998; Otto, 2001),
certain partial differential equations can be seen as coming from a variational principle, i.e., they
perform steepest descent with respect to functionals of their state distribution. Section 3 is a
generalization of this idea, we give a short overview here with the heat equation. The heat equation

_ρt = ∇_ _·_ (∇ρ) _,_

can be written as the steepest descent for the Dirichlet energy functional


1
2


�

Ω _[|][∇][ρ][|][2][ dx][.]_


However, the same PDE can also be seen as the gradient flow of the negative Shannon entropy in the
Wasserstein metric (Santambrogio, 2017; 2015),

�
_−H(ρ) =_

Ω _[ρ][(][x][)]_ [log] _[ρ][(][x][)][ dx][.]_

More precisely, the sequence of iterated minimization problems


_ρk[τ]+1_ _[∈]_ [arg min]
_ρ_


� 2[(][ρ][,] _[ρ]k[τ]_ [)]
_−H(ρ)+_ [W][2]
2τ


�
(A6)


converges to trajectories of the heat equation as τ → 0. This equivalence is extremely powerful
because it allows us to interpret, and modify, the functional −H(ρ) that PDEs such as the heat
equation implicitly minimize.

This equivalence is also quite natural, the heat equation describes the probability density of pure√
Brownian motion: dx = 2 dW (t). The Wasserstein point-of-view suggests that Brownian motion

maximizes the entropy of its state distribution, while the Dirichlet functional suggests that it minimizes
the total-variation of its density. These are equivalent. While the latter has been used extensively in
image processing, our paper suggests that the entropic regularization point-of-view is very useful to
understand SGD for machine learning.

### E EXPERIMENTAL SETUP

We consider the following three networks on the MNIST (LeCun et al., 1998) and the CIFAR-10 and
CIFAR-100 datasets (Krizhevsky, 2009).

(i) small-lenet: a smaller version of LeNet (LeCun et al., 1998) on MNIST with batchnormalization and dropout (0.1) after both convolutional layers of 8 and 16 output channels,
respectively. The fully-connected layer has 128 hidden units. This network has 13, 338 weights
and reaches about 0.75% training and validation error.

(ii) small-fc: a fully-connected network with two-layers, batch-normalization and rectified linear
units that takes 7 × 7 down-sampled images of MNIST as input and has 64 hidden units.
Experiments in Section 4.2 use a smaller version of this network with 16 hidden units and 5
output classes (30, 000 input images); this is called tiny-fc.

(iii) small-allcnn: this a smaller version of the fully-convolutional network for CIFAR-10 and
CIFAR-100 introduced by Springenberg et al. (2014) with batch-normalization and 12, 24
output channels in the first and second block respectively. It has 26, 982 weights and reaches
about 11% and 17% training and validation errors, respectively.

We train the above networks with SGD with appropriate learning rate annealing and Nesterov’s
momentum set to 0.9. We do not use any data-augmentation and pre-process data using global
contrast normalization with ZCA for CIFAR-10 and CIFAR-100.


-----

We use networks with about 20, 000 weights to keep the eigen-decomposition of D(x) ∈ R[d][×][d]

tractable. These networks however possess all the architectural intricacies such as convolutions,
dropout, batch-normalization etc. We evaluate D(x) using (2) with the network in evaluation mode.

### F PROOFS

F.1 THEOREM 5

The KL-divergence is non-negative: F(ρ) ≥ 0 with equality if and only if ρ = ρ [ss]. The expression
in (11) follows after writing
log _ρ_ [ss] = −β Φ _−_ log _Z(β_ ).

We now show that _[dF]dt[(][ρ][)]_ _≤_ 0 with equality only at ρ = ρ [ss] when F(ρ) reaches its minimum and the

Fokker-Planck equation achieves its steady-state. The first variation (Santambrogio, 2015) of F(ρ)
computed from (11) is
_δ_ _F_
_δρ_ [(][ρ][) =][ Φ][(][x][)+] _[β][ −][1][�]_ log _ρ +_ 1�, (A7)

which helps us write the Fokker-Planck equation (FP) as


� � _δ_ _F_
_ρt = ∇_ _·_ _−_ _j ρ +_ _ρ D ∇_

_δρ_


��
_._ (A8)


Together, we can now write

_dF(ρ)_ � _δ_ _F_

=
_dt_ _x∈Ω_ _[ρ][t]_ _δρ_ _[dx]_


� _δ_ _F_ � _δ_ _F_ � � _δ_ _F_ ��
= _ρ D ∇_ _dx._

_x∈Ω_ _δρ_ [∇] _[·]_ [(][−] _[j][ ρ][)][ dx]_ [+] _x∈Ω_ _δρ_ [∇] _[·]_ _δρ_


As we show in Appendix B, the first term above is zero due to Assumption 4. Under suitable boundary
condition on the Fokker-Planck equation which ensures that no probability mass flows across the
boundary of the domain ∂ Ω, after an integration by parts, the second term can be written as

_dF(ρ)_ � � �� �⊤

= − ∇ _[δ]_ _[F]_ ∇ _[δ]_ _[F]_ _dx_
_dt_ _x∈Ω_ _[ρ][ D][ :]_ _δρ_ [(][ρ][)] _δρ_ [(][ρ][)]


_≤_ 0.

In the above expression, A : B denotes the matrix dot product A : B = ∑ij AijBij. The final inequality
with the quadratic form holds because D(x) ⪰ 0 is a covariance matrix. Moreover, we have from (A7)
that
_dF(ρ_ [ss])

= 0.
_dt_

F.2 LEMMA 6

The forward implication can be checked by substituting ρ [ss](x) ∝ _e[−][c][ β][ f]_ [(][x][)] in the Fokker-Planck
equation (FP) while the reverse implication is true since otherwise (A4) would not hold.

F.3 LEMMA 7

The Fokker-Planck operator written as

_L ρ = ∇_ _·_ �− _j ρ + D ∇Φ ρ −_ _β_ _[−][1]_ (∇ _·_ _D) ρ +_ _β_ _[−][1]∇_ _·_ (D ρ)�

from (8) and (FP) can be split into two operators

_L = LS +_ _LA,_


-----

where the symmetric part is

_LS ρ = ∇_ _·_ �D ∇Φ ρ − _β_ _[−][1]_ (∇ _·_ _D) ρ + β_ _[−][1]∇_ _·_ (D ρ)� (A9)

and the anti-symmetric part is

_LA ρ = ∇_ _·_ (− _jρ)_

= ∇ _·_ �−D ∇Φ ρ + ∇ _f_ _ρ +_ _β_ _[−][1](∇_ _·_ _D)ρ�_ (A10)

= ∇ _·_ �β _[−][1]_ _D ∇ρ + ∇_ _f_ _ρ +_ _β_ _[−][1](∇_ _·_ _D)ρ�_ _._

We first note that LA does not affect F(ρ) in Theorem 5. For solutions of ρt = LA ρ, we have

_d_ � _δ_ _F_
_dt [F][(][ρ][) =]_ Ω _δρ [ρ][t][ dx]_


� _δ_ _F_
= Ω _δρ_ [∇] _[·]_ [(][−] _[j][ ρ][)][ dx]_

= 0,

by Assumption 4. The dynamics of the anti-symmetric operator is thus completely deterministic and
conserves F(ρ). In fact, the equation (A10) is known as the Liouville equation (Frank, 2005) and
describes the density of a completely deterministic dynamics given by

_x˙ = j(x);_ (A11)

where j(x) = J[ss]/ρ [ss] from Appendix C. On account of the trajectories of the Liouville operator being
deterministic, they are also the most likely ones under the steady-state distribution ρ [ss] ∝ _e[−][β]_ [Φ].

F.4 THEOREM 22

All the matrices below depend on the weights x; we suppress this to keep the notation clear. Our
original SDE is given by
_dx = −∇_ _f dt +_ �2β _[−][1]_ _D dW_ (t).

We will transform the original SDE into a new SDE


_G dx = −∇Φ dt +_ �


2β _[−][1]_ _S dW_ (t) (A12)


where S and A are the symmetric and anti-symmetric parts of G[−][1],

_S =_ _[G][−][1][ +]_ _[G][−][T]_ _,_

2

_A = G[−][1]_ _−_ _S._


Since the two SDEs above are equal to each other, both the deterministic and the stochastic terms
have to match. This gives
∇ _f_ (x) = G ∇Φ(x)

_D =_ _[G]_ [+] _[G][⊤]_

2

_Q =_ _[G]_ _[−]_ _[G][⊤]_ _._

2

Using the above expression, we can now give an explicit, although formal, expression for the potential:


� 1
Φ(x) =

0


� �
_G[−][1](Γ(s)) ∇_ _f_ (Γ(s)) _·_ _dΓ(s);_ (A13)


where Γ : [0, 1] → Ω is any curve such that Γ(1) = x and Γ(0) = x(0) which is the initial condition of
the dynamics in (3). Note that Φ(x) does not depend on β because G(x) does not depend on β .


-----

We now write the modified SDE (A12) as a second-order Langevin system after introducing a velocity
variable p with q ≜ _x and mass m:_

_dq =_ _[p]_

_m [dt]_

(A14)

_dp = −_ (S + _A)_ _[p]_ �2β _[−][1]_ _S dW_ (t).

_m [dt][ −]_ [∇][q][Φ][(][q][)][ dt][ +]


The key idea in Yin and Ao (2006) is to compute the Fokker-Planck equation of the system above
and take its zero-mass limit. The steady-state distribution of this equation, which is also known as the
Klein-Kramer’s equation, is


1 �
_ρ_ [ss](q, p) = _−β Φ(q)_ _−_ _[β][ p][2]_
_Z[′](β_ ) [exp] 2m


�
; (A15)


where the position and momentum variables are decoupled. The zero-mass limit is given by

_ρt = ∇_ _·_ _G_ �∇Φ ρ + _β_ _[−][1]_ ∇ρ�,

= ∇ _·_ �D ∇Φ ρ + _Q ∇Φ ρ +(D_ + _Q) β_ _[−][1]_ ∇ρ�


(A16)


= ∇ _·_ �D ∇Φ ρ + _Q ∇Φ ρ�_ + ∇ _·_ �D β _[−][1]_ ∇ρ� + _β_ _[−][1]_ ∇ _·_ (Q ∇) ρ

� ��∗ �


We now exploit the fact that Q is defined to be an anti-symmetric matrix. Note that ∑i, _j ∂i∂_ _j (Qijρ) = 0_
because Q is anti-symmetric. Rewrite the third term on the last step (∗) as

� �
∇ _·_ (Q ∇ρ) = ∑ _∂i_ _Qij ∂_ _jρ_
_ij_


� �
= −∑ _∂i_ _∂_ _jQij_ _ρ_
_ij_

� �
= −∇ _·_ ∇ _·_ _Q_ _ρ._


(A17)


We now use the fact that (3) has ρ [ss] ∝ _e[−][β]_ [Φ] as the steady-state distribution as well. Since the
steady-state distribution is uniquely determined by a Fokker-Planck equation, the two equations (FP)
and (A16) are the same. Let us decompose the second term in (FP):


_β_ _[−][1]_ ∑ _∂i∂_ _j�Dij(x)ρ(x)�_
_i,_ _j_

= β _[−][1]_ ∑ _∂i�_ (∂ _jDij)_ _ρ�_
_i,_ _j_


+ _β_ _[−][1]_ ∑ _∂i�Dij∂_ _jρ�._
_i,_ _j_


Observe that the brown terms are equal. Moving the blue terms together and matching the drift terms
in the two Fokker-Planck equations then gives

∇ _f = (D_ + _Q) ∇Φ_ _−_ _β_ _[−][1]∇_ _·_ _D_ _−_ _β_ _[−][1]∇_ _·_ _Q_

The critical points of Φ are different from those of the original loss f by a term that is β _[−][1]∇_ _· (D_ + _Q)._


-----

