# diffeq

I'm learning about differential equations. I'm starting off with the [MIT OCW](https://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/video-lectures/) course, but I'm going to incorporate other sources as well.

# Notes

Here are some high-level notes that I'll jot down as I go through my self-made curriculum.

## MIT OCW

Here's some of the high-level stuff that I learned from the MIT course:

 * Lecture 1: The Geometrical View
   * Solutions are functions, not numbers. Reminds me of ML.
   * Solutions can be found by integrating over the direction field. This is Euler's method.
 * Lecture 2: Numerical Methods
   * Euler's method has O(h) error.
   * RK2 has O(h^2) error.
   * RKn has O(h^n) error.
 * Lecture 3: First-order Linear ODEs
   * Always admit a solution (involves an integral, though).
   * "Integrating factors" are the general way to solve these problems.

## My own work

Here's some of the high-level stuff that I learned via my own derivations or thinking:

 * Numerical methods
   * Error analysis can be performed via Taylor series.
     * The error on one step of Euler's method is O(h^2). That's why k/h steps is O(h).
     * The error on one step of RK2 is O(h^3).
   * New methods can be derived using Taylor series and solving a system to knock out the low-order terms:
     * [I derived a third-order method](derivations/third_order.jpg), which I believe is a variant of RK3.
     * I derived a fourth-order method that requires 6 function evals. See `derivations/fourth_order_*.jpg`.
