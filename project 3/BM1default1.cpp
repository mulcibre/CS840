#include <iostream>
using namespace std;

#include<time.h>

int IFcnt[5],IFEcnt[5],SWcnt[5],WHILEcnt[5],DOcnt[5],FORcnt[5];

int F1(void)
{
   int a,b,c,d,e,f,g,h,i,j,k,l,m,n;
   a=b=c=d=e=f=g=h=i=j=k=l=m=n=1;
   do
   {
      m += (m+k-c*l+f*f*a*e+c-c-a)%100;
      if( ++IFEcnt[0]%2 )
      {
         g += (g-c-i)%100;
         c  = (a*b-e*g+j+l-g-h-c)%100;
         i += (f+a+a+h)%100;
         j -= (h-k+g)%100;
         j += (e-m-n+g+b-i+i+e*l+f+c-j-h*e)%100;
      }
      else
      {
         
         switch( ++SWcnt[0]%3 )
         {

         case 1:
         {
            while( ++WHILEcnt[0]%5 )
            {
               do
               {
                  i += (g+h-b+c-h-n+i-j)%100;
                  d += (j+l)%100;
                  k -= (j+k*k*m+n+c*b+i+i)%100;
               } while( ++DOcnt[1]%5 );
               for( ; ++FORcnt[0]%5 ; )
               {
                  n -= (h+g)%100;
                  j  = (n-j-l-f-e-h+j-a-a-b)%100;
                  h += (h+g+b-i+m-a*g-a*a)%100;
                  l += (h+a)%100;
                  h += (m*c*e-k+f+m+d-h+i+n)%100;
               }
               m += (m+a+h-a-a*a*b-n*m+e-h*m+g-k)%100;
               d -= (f+d+c-m-d+f+h+j+h+l-j-d+b)%100;
               j -= (f-n*f*d-l-n*c-l*j-n-c+b)%100;
            }
            l += (g+n)%100;
            e += (a-j-a)%100;
            e += (l-m*m+a+k*c+h+j)%100;
            i += (d+i-b*e+g-a+j*k-b-d+h+g-c-a)%100;
            c += (a+j)%100;
         }
         break;

         case 2:
         {
            m += (h+j-c-n*j-h-f*k)%100;
            h -= (e*m+c-i-j+e+j-l-j*b+m+c+b+m)%100;
            e  = (e*d)%100;
            l -= (f*c)%100;
         }
         break;

         default:
         {
            i  = (a-h+f-d-b*l*m+g-n*m-d*l*i)%100;
            l  = (d-l+l+c+k+k-h*n)%100;
            j -= (j+k)%100;
            c -= (h+d-m+n*b)%100;
            j -= (i-e*i+a*e)%100;
            n -= (a*n+h-a+h+g+d*c-h+n-i-c)%100;
         }
         }

         j  = (c-a+e*k*j-f+g)%100;
         f -= (b+b)%100;
         b += (e+c-f+l-g-g-f+a+l*n+b)%100;
      }
      c += (e*j+f*j*k-h+c*i*a-d*c)%100;
      f += (l+i+e+j+b+i+c)%100;
      d += (j-b+n)%100;
   } while( ++DOcnt[0]%5 );
   e -= (a-d*g)%100;
   b += (c-h-h*m+j*m-l+c-e+g-c+l+c)%100;
   f  = (g+l-k+d-b*b+f+c-k-i+j*l*m)%100;
   f += (n+h-n-m-m-c*b-k+l*b-g+j)%100;
   d -= (m*n+l-f-i*n-d)%100;
   d -= (k+e*c-a-d+d)%100;
   e -= (g+l+i+e)%100;
   return (a+b+c+d+e+f+g+h+i+j+k+l+m+n)%100 ;
}

int F2(void)
{
   int a,b,c,d,e,f,g,h,i,j,k,l,m,n;
   a=b=c=d=e=f=g=h=i=j=k=l=m=n=1;
   e += (f+j+g-c+e-m-b+g-a)%100;
   f  = (k+a-n+g-i-i-c+e-g-n-l-m+d-c)%100;
   c -= (a-h-k-m+a+k+b+j)%100;
   m += (l-f)%100;
   g += (j-i-h*n)%100;
   l += (i+m+g-n+l-a+k-n+i*l+b+m+g+h)%100;
   f += (j-j)%100;
   k -= (a+g*k-m-n)%100;
   return (a+b+c+d+e+f+g+h+i+j+k+l+m+n)%100 ;
}

int main(void)
{
   int I;
   clock_t StartTick = clock();
   for(I=0; I<5; I++) IFcnt[I]   =0;
   for(I=0; I<5; I++) IFEcnt[I]  =0;
   for(I=0; I<5; I++) SWcnt[I]   =0;
   for(I=0; I<5; I++) WHILEcnt[I]=0;
   for(I=0; I<5; I++) DOcnt[I]   =0;
   for(I=0; I<5; I++) FORcnt[I]  =0;
   long int sum=0;

   sum += F1( ) ;
   sum += F2( ) ;

   cout << "\nChecksum = " << sum;
   for(I=sum=0; I<0; I++) sum += IFcnt[I];
   cout << "\nIF frequency:      Static = " << 0 << "   Dynamic = " << sum ;
   for(I=sum=0; I<1; I++) sum += IFEcnt[I];
   cout << "\nIF-ELSE frequency: Static = " << 1 << "   Dynamic = " << sum ;
   for(I=sum=0; I<1; I++) sum += SWcnt[I];
   cout << "\nSWITCH frequency:  Static = " << 1 << "   Dynamic = " << sum ;
   for(I=sum=0; I<1; I++) sum += WHILEcnt[I];
   cout << "\nWHILE frequency:   Static = " << 1 << "   Dynamic = " << sum ;
   for(I=sum=0; I<2; I++) sum += DOcnt[I];
   cout << "\nDO frequency:      Static = " << 2 << "   Dynamic = " << sum ;
   for(I=sum=0; I<1; I++) sum += FORcnt[I];
   cout << "\nFOR frequency:     Static = " << 1 << "   Dynamic = " << sum ;
   cout << "\nRun Time = " << double(clock()-StartTick)/CLOCKS_PER_SEC << " sec\n\n";

   return 0;
}