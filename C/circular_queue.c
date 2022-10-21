#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct queue
{
    int front, rear;
    int capacity;
    int size;
    int *arr;
};

// Create a queue
struct queue *createQueue(int capacity)
{
    struct queue *Q = malloc(sizeof(struct queue));
    if (!Q)
    {
        /* code */
        return NULL;
    }
    Q->capacity = capacity;
    Q->size = 0;
    Q->front = Q->rear = -1;
    Q->arr =(int*) malloc(Q->capacity * sizeof(int));

    if (!Q->arr)
    {
        /* code */
        return NULL;
    }

    return Q;
}

int size(struct queue *Q)
{
    return Q->size ;
}

int frntEle(struct queue *Q)
{
    return Q->arr[Q->front];
}

int rearEle(struct queue *Q)
{
    return Q->arr[Q->rear];
}

int isEmpty(struct queue *Q)
{
    return (Q->size == 0);
}

int isFull(struct queue *q)
{
    return (q->size == q->capacity);
}

void enQueue(struct queue *Q, int val)
{
    if (isFull(Q))
        printf("Queue overfloew \n");

    Q->rear = (Q->rear + 1) % (Q->size);
    Q->arr[Q->rear] = val;

    if(Q->front == -1)
        Q->front = Q->rear ;

    Q->size += 1;
}

int deQueue(struct queue *Q)
{
    int data = INT_MIN;
    if (isEmpty(Q))
    {
        printf("Queue underflow \n");
        return data;
    }

    data = Q->arr[Q->front];
    if (Q->front == Q->rear)
    {
        /* code */
        Q->rear = Q->front = -1;
        Q->size = 0;
    }

    else
    {
        Q->front = (Q->front + 1) % (Q->size);
        Q->size -= 1;
    }

    return data;
}

void deleteQueue(struct queue *Q)
{
    if (Q)
    {
        if (Q->arr)
            free(Q->arr);
        free(Q);
    }
}

void showQueue(struct queue* Q)
{
    for (int i = 0; i < Q->size ; i++)
    {
        /* code */
        printf("%d \n" , Q->arr[i]) ;
    }
    
}

int main()
{
    struct queue *Q;
    Q = createQueue(10);
    enQueue(Q, 67);
    enQueue(Q, 7);
    enQueue(Q, 9);
    enQueue(Q, 68989);

    // showQueue(Q) ;
    printf("%d" , isFull(Q)) ;
    printf("Size of the queue is - %d \n" , size(Q)) ;
    printf("Front element of the queue is - %d \n" , frntEle(Q)) ;
    printf("Rear element of the queue is - %d \n" , rearEle(Q)) ;

    deQueue(Q) ;
    deQueue(Q) ;
    deQueue(Q) ;

    printf("%d" , isEmpty(Q)) ;
    deleteQueue(Q) ;


    return 0;
}
