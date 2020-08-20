#### FFT

```c
struct FastFourierTransform  {
    Complex omega [N], omegaInverse [N] ;

    void init ( const int& n )  {
        for ( int i = 0 ; i < n ; ++ i )  {
            omega [i] = Complex ( cos ( 2 * PI / n * i), sin ( 2 * PI / n * i ) ) ;
            omegaInverse [i] = omega [i].conj ( ) ;
        }
    }

    void transform ( Complex *a, const int& n, const Complex* omega ) {
        for ( int i = 0, j = 0 ; i < n ; ++ i )  {
		if ( i > j )  std :: swap ( a [i], a [j] ) ;
		for( int l = n >> 1 ; ( j ^= l ) < l ; l >>= 1 ) ;
	}

        for ( int l = 2 ; l <= n ; l <<= 1 )  {
            int m = l / 2;
            for ( Complex *p = a ; p != a + n ; p += l )  {
                for ( int i = 0 ; i < m ; ++ i )  {
                    Complex t = omega [n / l * i] * p [m + i] ;
                    p [m + i] = p [i] - t ;
                    p [i] += t ;
                }
            }
        }
    }

    void dft ( Complex *a, const int& n )  {
        transform ( a, n, omega ) ;
    }

    void idft ( Complex *a, const int& n )  {
        transform ( a, n, omegaInverse ) ;
        for ( int i = 0 ; i < n ; ++ i ) a [i] /= n ;
    }
} fft ;
```

