# diffeq

Learning differential equations from the [MIT OCW](https://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/video-lectures/) course.

# High-level notes

Here's some of the high-level stuff that I learned:

 * Lecture 1: The Geometrical View
   * Solutions are functions, not numbers. Reminds me of ML.
   * Solutions can be found by integrating over the direction field. This is Euler's method.
 * Lecture 2: Numerical Methods
   * Euler's method has O(h) error.
   * RK2 has O(h^2) error.
   * RKn has O(h^n) error.
   * My own derivations:
     * The error on one step of Euler's method is O(h^2). That's why k/h steps is O(h).
     * The error on one step of RK2 is O(h^3).
     * [I derived a third-order method](derivations/third_order.jpg), which I believe is a variant of RK3.
 * Lecture 3: First-order Linear ODEs
   * Always admit a solution (involves an integral, though).
   * "Integrating factors" are the general way to solve these problems.
