{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8554fd6e-ecd3-424e-bb7d-3b443734f8ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the password : MAnish@#$1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid Password\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Q-1: You are writing code for a company.The requirement of the company is that you create\n",
    "        a python function that will check whether the password entered by the user is correct or not.The\n",
    "        function should take the password as input and return the string \"Valid Password\" if the enetered \n",
    "        password follows the below-given password guidlines else it should return \"Invalid Password\".\n",
    "        \n",
    "        Note: 1. The Password should contain at least two uppercase letters and at least two lowercase \n",
    "        letters.\n",
    "              2. The Password should cotain at least a number and three special characters.\n",
    "              3. The length of the password should be 10 characters long.   \"\"\"\n",
    "\n",
    "def password_checker(password):\n",
    "    u,l,n,s=0,0,0,0\n",
    "    \n",
    "    if(len(password)==10):\n",
    "    \n",
    "        for i in password:           \n",
    "        \n",
    "            if(i.isupper()):\n",
    "                u+=1               # count uppercase letters \n",
    "            if(i.islower()):\n",
    "                l+=1               # count lowercase letters\n",
    "            if(i.isdigit()):\n",
    "                n+=1               # count digits \n",
    "            if(i==\"@\" or i==\"$\" or i==\"#\" or i==\"_\"):\n",
    "                s+=1               # count special characters\n",
    "        \n",
    "        if(u>=2 and l>=2 and n>=1 and s==3 and u+l+n+s==len(password)):\n",
    "            print(\"Valid Password\")\n",
    "        else:\n",
    "            print(\"Invalid Password\")\n",
    "            \n",
    "            \n",
    "password=input(\"Enter the password :\")\n",
    "password_checker(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "beeaa62c-f45f-488e-813e-7d41af2f225d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the string: python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Q-2: Solve the below-given questions using at least one of the following:\n",
    "        \n",
    "        1.lambda function\n",
    "        2.Filter function\n",
    "        3.Map function\n",
    "        4.list comprehension \n",
    "        \n",
    "         (i) Check if the string starts with a particular letter.\n",
    "        (ii) Check if the string is numeric.\n",
    "       (iii) Sort a list of tuples having fruit names and their quantity.\n",
    "            [(\"mango\",99),(\"orange\",80),(\"grapes\",10000)]\n",
    "       (iv)  Find the squares of numbers from 1 to 10.\n",
    "        (v)  Find the cube root of numbers from 1 to 10.\n",
    "       (vi)  Check if a given number is even\n",
    "      (vii)  Filter odd numbers from given list.\n",
    "             [1,2,3,4,5,6,7,8,9,10]\n",
    "     (viii)  Sort a list of integers into positive and negative integers lists.\n",
    "            [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]      \"\"\"\n",
    "# (i) Check if the string starts with a particular letter.\n",
    "\n",
    "str=input(\"Enter the string:\")\n",
    "starts_with=lambda x: True if x.startswith('P') or x.startswith('p') else False\n",
    "print(starts_with(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3d63a167-de41-4061-a2e4-fd43de624bfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the string: 34\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# (ii) Check if the string is numeric.\n",
    "\n",
    "str=input(\"Enter the string:\")\n",
    "is_numeric=lambda x: True if x.isnumeric() else False\n",
    "print(is_numeric(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "225f7a8d-5b3a-4e21-ba9f-d6bd26408613",
   "metadata": {},
   "outputs": [],
   "source": [
    "#  (iii) Sort a list of tuples having fruit names and their quantity.\n",
    "#            [(\"mango\",99),(\"orange\",80),(\"grapes\",10000)]\n",
    "\n",
    "l=[(\"mango\",99),(\"orange\",80),(\"grapes\",10000)]\n",
    "\n",
    "l1=sorted(l,key=lambda x: x[0],reverse=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5da672c6-d1fd-40fe-8398-ad6f9c828645",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('orange', 80), ('mango', 99), ('grapes', 10000)]\n"
     ]
    }
   ],
   "source": [
    "print(l1) # sorted by fruits name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0673a04a-72be-4807-8fde-3c62167a67f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('orange', 80), ('mango', 99), ('grapes', 10000)]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "l=[(\"mango\",99),(\"orange\",80),(\"grapes\",10000)]\n",
    "\n",
    "l1=sorted(l,key=lambda x: x[1],reverse=False)\n",
    "print(l1) # sorted by quantity \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f16d425f-141d-400c-b0e8-53550c3260d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# (iv)  Find the squares of numbers from 1 to 10.\n",
    "\n",
    "sq=list(map(lambda x: x**2,range(1,11)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9dfb55a3-7855-45b0-80d2-ab96b051ae3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "print(sq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b5ad011b-c83d-41d0-bdec-271f5a781247",
   "metadata": {},
   "outputs": [],
   "source": [
    "# (v)  Find the cube root of numbers from 1 to 10.\n",
    "\n",
    "cube=list(map(lambda x: x**(1/3),range(1,11)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f5039bd0-7531-46db-a268-1367b7098b08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968, 1.8171205928321397, 1.912931182772389, 2.0, 2.080083823051904, 2.154434690031884]\n"
     ]
    }
   ],
   "source": [
    "print(cube)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9345b721-bcba-4f8d-8112-19a10d1618f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even\n"
     ]
    }
   ],
   "source": [
    "# (vi)  Check if a given number is even.\n",
    "\n",
    "num=int(input(\"Enter a number\"))\n",
    "even=(lambda x: \"Even\" if x%2==0 else \"odd\")\n",
    "print(even(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "05bca969-fc02-48a0-a86a-63e9a5bd8626",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd Number: [1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "# (vii)  Filter odd numbers from given list.\n",
    "number=[1,2,3,4,5,6,7,8,9,10]\n",
    "odd=list(filter(lambda x: x%2!=0,number))\n",
    "print(\"Odd Number:\", odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "14c3bc0c-c208-4f64-8a1d-a4c9b744509b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive Integer [2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "# (viii)  Sort a list of integers into positive and negative integers lists.\n",
    "           \n",
    "l = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0] # the number zero (0) is neither positive nor negative\n",
    "p=[i for i in l if i>1] # list comprehension\n",
    "    \n",
    "print(\"Positive Integer\",p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a0c0d821-380c-47e1-8218-a66a598c6f0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Negative Integer [-1, -2, -3, -4, -5, 0]\n"
     ]
    }
   ],
   "source": [
    "N=[i for i in l if i < 1]\n",
    "print(\"Negative Integer\",N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55434224-fc49-4df9-b2ad-777de43b2723",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
