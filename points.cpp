#include <iostream>
using namespace std;

struct Point {
    int x, y;
};

void affiche(const Point &point){
    cout << point.x << " " << point.y << endl;
}

void modif_point1(Point point){
    point.x++;
}

void modif_point2(Point *point){
    (*point).y++;
}

void modif_point3(Point & point){
    point.x--;
    point.y--;
}

int main(){
    Point point;
    Point tab[3] = {{1,2},{2,4},{3,6}};
    point.x = 45;
    point.y = 12;

    for(auto & elem : tab){
        affiche(elem);
        modif_point3(elem);
    }
    for(const Point & elem : tab){
        affiche(elem);
    }

    affiche(point);
    modif_point1(point);
    affiche(point);
    modif_point2(&point);
    affiche(point);
    modif_point3(point);
    affiche(point);

    return 0;
}
