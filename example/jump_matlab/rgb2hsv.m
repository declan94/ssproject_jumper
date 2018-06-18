function [ h,s,v ] = rgb2hsv( r,g,b )
%RGB2HSV 此处显示有关此函数的摘要
%   此处显示详细说明
    r=r/255.0;
    g=g/255.0;
    b=b/255.0;
%     mx=max(r,g,b);
%     mn=min(r,g,b);
    mx=max(r,g);
    mx=max(mx,b);
    mn=min(r,g);
    mn=min(mn,b);
    df = mx-mn;
    if mx==mn
        h=0;
    elseif mx==r
        h=mod(60.*((g-b)/df)+360,360);
    elseif mx==g
        h=mod(60.*((b-r)/df)+120,360);
    elseif mx==b
        h=mod(60.*((r-g)/df)+240,360);
    end
    
    if mx==0
        s=0;
    else
        s=df/mx;
    end
    v=mx;
end

