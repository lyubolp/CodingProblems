#include <iostream>
#include <math.h>
#include <algorithm>

class Point {
public:
    Point(): x(0), y(0) {}
    Point(const double x, const double y): x(x), y(y) {}

    double get_x() const {
        return this->x;
    }

    double get_y() const {
        return this->y;
    }

    Point get_centerpoint(const Point& b, const double& percentage=0.5) const {
        double center_p1_p2_x = this->x + (b.get_x() - this->x) * percentage;
        double center_p1_p2_y = this->y + (b.get_y() - this->y) * percentage;

        return Point(center_p1_p2_x, center_p1_p2_y);
    }

    double get_distance_to(const Point& b) const {
        return sqrt(pow((this->x - b.get_x()), 2) +  pow((this->y - b.get_y()), 2));
    }

    Point scale(const double& factor) const{
        return Point(this->x * factor, this->y * factor);
    }

    Point translate(const Point& factor) const{
        return Point(this->x + factor.x, this->y + factor.y);
    }

    Point operator-(const Point& other) {
        return Point(this->x - other.x, this->y - other.y);
    }
private:
    double x;
    double y;
};

std::istream& operator>> (std::istream& is, Point& p) {
    double x, y;
    is >> x >> y;

    p = Point(x, y);

    return is;
}
std::ostream& operator<< (std::ostream& os, const Point& p) {
    if (p.get_x() >= 0 && p.get_y() >= 0) {
        os << "(" << p.get_x() << ", " << p.get_y() << ")";
    }
    else if (p.get_x() < 0 && p.get_y() >= 0) {
        os << "(-" << p.get_x() << ", " << p.get_y() << ")";
    }
    else if (p.get_x() >= 0 && p.get_y() < 0) {
        os << "(" << p.get_x() << ", -" << p.get_y() << ")";
    }
    else {
        os << "(-" << p.get_x() << ", -" << p.get_y() << ")";
    }
    return os;
}


class Line{
public:
    Line(const Point& A, const Point& B) {
        this->a = B.get_y() - A.get_y();
        this->b = A.get_x() - B.get_x();
        this->c = a * A.get_x() + b * A.get_y();

        // We get the line in ax + by = c
        // But we want it to be in the format y = ax + c
        // So we need to do y = (c - ax)/b => c/b - (a/b)x

        this->a *= -1;

        if (this->b != 0) {
            this->a /= this->b;
            this->c /= this->b;
            this->b = 1;
        }
    }

    double get_a() const {
        return this->a;
    }

    double get_b() const {
        return this->b;
    }

    double get_c() const {
        return this->c;
    }

    Point get_crosspoint(const Line& other) const {
        double x, y;

        if (this->a == 0) {
            y = this->c;
            x = (y - other.c)/other.a;
        }
        else if (this->b == 0) {
            x = -1 * (this->c/this->a);
            y = other.a * x + other.c;
        }
        else if (other.a == 0 || other.b == 0) {
            return other.get_crosspoint(*this);
        }
        else {
            x = (other.c - this->c) / (this->a - other.a);
            y = this->a * x + this->c;
        }
        
        return Point(x, y);
    }
private:
    double a;
    double b;
    double c;

    static double calculate_a(const Point& A, const Point& B) {
        return (abs(A.get_y() - B.get_y())) / (abs(A.get_x() - B.get_x()));
    }
};
std::ostream& operator<< (std::ostream& os, const Line& l) {
    if (l.get_b() >= 0) {
        os << l.get_b() << "y = " << l.get_a() << "x + " << l.get_c();
    }
    else {
        os << "-" << l.get_b() << "y = " << l.get_a() << "x + " << l.get_c();
    }
    
    return os;
}

class Triangle {
public:
    Triangle(const Point& p1, const Point& p2, const Point& p3): p1(p1), p2(p2), p3(p3) {}

    Point get_centroid() const {
        Point center_p1_p2 = this->p1.get_centerpoint(this->p2, 0.5);

        double one_third = 1.0/3.0;
        Point center_p1_p2_p3 = center_p1_p2.get_centerpoint(this->p3, one_third);

        return center_p1_p2_p3;
    }

    double get_perimiter() const {
        double side_p1_p2 = this->p1.get_distance_to(this->p2);
        double side_p1_p3 = this->p1.get_distance_to(p3);
        double side_p2_p3 = this->p2.get_distance_to(p3);

        return side_p1_p2 + side_p1_p3 + side_p2_p3;
    }

    Triangle scale(const double& factor) const {
        Point centroid = this->get_centroid();
        Point new_p1 = this->p1.scale(factor) - centroid;
        Point new_p2 = this->p2.scale(factor) - centroid;
        Point new_p3 = this->p3.scale(factor) - centroid;
        return Triangle(new_p1, new_p3, new_p3);
    }

    Triangle translate(const Point& factor) const {
        return Triangle(this->p1.translate(factor), this->p2.translate(factor), this->p3.translate(factor));
    }

    Point get_p1() const {
        return this->p1;
    }

    Point get_p2() const {
        return this->p2;
    }

    Point get_p3() const {
        return this->p3;
    }
private:
    Point p1;
    Point p2;
    Point p3;
};
std::ostream& operator<< (std::ostream& os, const Triangle& triangle) {
    os << triangle.get_p1() << ", " << triangle.get_p2() << ", " << triangle.get_p3();
    return os;
}

int main() {

    // Point a1, a2, b1, b2, c1, c2, n;
    // std::cin >> a1 >> a2 >> b1 >> b2 >> c1 >> c2 >> n;

    // Line a(a1, a2), b(b1, b2), c(c1, c2);

    // //1. Get the cross point of the lines (K', L', M')
    // Point p1 = a.get_crosspoint(b);
    // Point p2 = a.get_crosspoint(c); 
    // Point p3 = b.get_crosspoint(c); 

    // //2. Find the centroid of the newly created triangle (K'L'M' ~ KLM)
    // Triangle prim(p1, p2, p3);
    // Point prim_triangle_centroid = prim.get_centroid();
    
    // //3. Find the translation matrix between (K'L'M' ~ KLM)
    // Point translation = Point(n.get_x() - prim_triangle_centroid.get_x(), n.get_y() - prim_triangle_centroid.get_y());
    
    // //4. Find the scale matrix between (P(K'L'M') = P(KLM)*s)
    // double current_perimeter = prim.get_perimiter();

    // double target_perimeter_a = a1.get_distance_to(a2);
    // double target_perimeter_b = b1.get_distance_to(b2);
    // double target_perimeter_c = c1.get_distance_to(c2);
    // double target_perimeter = target_perimeter_a + target_perimeter_b + target_perimeter_c;

    // double scale_factor = target_perimeter / current_perimeter;

    // //5. Calculate the new points K, L and M
    // Triangle result = prim.translate(translation).scale(scale_factor);
    // std::cout << result << std::endl;

    Point A(1, 1), B(3, 1), C(1, 4), D(5, 5);

    Triangle t1(A, B, C);
    std::cout << t1 << std::endl;
    
    Triangle t2 = t1.translate(D - t1.get_centroid());
    std::cout << t2 << std::endl;
    
    Triangle t3 = t2.scale(1.5);
    std::cout << t3 << std::endl;
    return 0;
}