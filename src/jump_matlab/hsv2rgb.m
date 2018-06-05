function [ r,g,b ] = hsv2rgb( h,s,v )
%HSV2RGB 此处显示有关此函数的摘要
%   此处显示详细说明
%     h=float(h);
%     s=float(s);
%     v=float(v);
    h=double(h);
    s=double(s);
    v=double(v);
    h60=h/60.0;
    h60f=floor(h60);
    hi=mod(int16(h60f),6);
    f=h60-h60f;
    p=v*(1-s);
    q=v*(1-f*s);
    t=v*(1-(1-f)*s);
    r=0;
    g=0;
    b=0;
    if hi==0
        r=v;
        g=t;
        b=p;
    elseif hi==1
        r=q;
        g=v;
        b=p;
    elseif hi==2
        r=p;
        g=v;
        b=t;
    elseif hi==3
        r=p;
        g=q;
        b=v;
    elseif hi==4
        r=t;
        g=p;
        b=v;
    elseif hi==5
        r=v;
        g=p;
        b=q;
    end
    r=int16(r*255);
    g=int16(g*255);
    b=int16(b*255);
end

