#include <iostream>
#include <string>

using std::string;

int edit_distance(const string &str1, const string &str2) {
  //write your code here
  int size1 = str1.length();
  int size2 = str2.length();
  int match2=0;
  int mismatch2=0;
  int d[size1+1][size2+1];
  d[0][0]=0;
  for(int i = 1; i<=str1.length();i++)
    {
      d[i][0] = i;

    }

  for(int j = 1; j<=str2.length();j++)
    {
      d[0][j] = j;

    }
  for(int j = 1; j<=size2;j++)
    {
      for (int i=1; i<=size1;i++)
	{

	  int insertion = d[i][j-1] +1;
	  int deletion = d[i-1][j] + 1;
	  int match = d[i-1][j-1];
	  int mismatch = d[i-1][j-1] + 1;

	  if(str1[i-1] == str2[j-1])
	    {
	      d[i][j] = std::min(std::min(insertion, deletion), match);
	      match2++;
	    }
	  else

	    {
	      d[i][j] = std::min(std::min(insertion, deletion), mismatch);
	      mismatch2++;
	    }
	}
    }
 
  return d[size1][size2];
}

int main() {
  string str1;
  string str2;
  std::cin >> str1 >> str2;
  std::cout << edit_distance(str1, str2) << std::endl;
  return 0;
}
