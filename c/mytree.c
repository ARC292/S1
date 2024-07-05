#include<stdio.h>
#include<stdlib.h>

struct t
{
 int data;
 struct t *l;
 struct t *r;
}

struct t *head=NULL;
struct t *root;

void ins()
{
   int data;
   printf("enter the element:");
   scanf("%d",&data)
   temp=(struct linn *)malloc(sizeof(struct linn));
  if(head==NULL)
  
  {
   
   head=temp;
   temp->l=NULL;
   temp->r=NULL;
   root=temp;
}

  if(root->l==NULL && root->r==NULL)
   {
     if(root->data>temp->data)
     {
       root->r=temp;
     }
     
    else
    {   
     root->l=temp;
    }
    
   if() 
     
}
