int ss(int n){
    int m = 0;
    while (n){
        m += (n % 10) * (n % 10);
        n /= 10;
    }
    return m;
}

bool isHappy(int n){
    int m = n;
    for (int i = 0; n > 1; i ^= 1) {
        n = ss(n);
        if (i)
            m = ss(m);
        if (n == m)
            return false;
    }
    return true;
}