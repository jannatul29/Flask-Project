PGDMP     (    0                 z            store #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1) #   12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16384    store    DATABASE     w   CREATE DATABASE store WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE store;
                postgres    false            �            1259    16508    hotel1    TABLE     /  CREATE TABLE public.hotel1 (
    id integer DEFAULT nextval('public.test12_id_seq'::regclass) NOT NULL,
    title character varying,
    herf character varying,
    image character varying,
    rating character varying,
    price character varying,
    location character varying,
    amenities text
);
    DROP TABLE public.hotel1;
       public         heap    postgres    false            �          0    16508    hotel1 
   TABLE DATA           \   COPY public.hotel1 (id, title, herf, image, rating, price, location, amenities) FROM stdin;
    public          postgres    false    223   H       \           2606    16516    hotel1 hotel1_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.hotel1
    ADD CONSTRAINT hotel1_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.hotel1 DROP CONSTRAINT hotel1_pkey;
       public            postgres    false    223            �     x��V�n�6}V�BO����&n�"�dC�L M�iPm��)C�㺏������S�%���Y:�dX �x�=�\�8��M8֏�&ȝ[,��p�^G3�ѳ(������f���3����]a,�f��vgZYg��j�f6�����Oa�\���@��"5@PA�#B�?_ɹ�<�}1�~]d.?��}�M1��	��CZW�W�L��8<�#5e������|L��m�jޛ��v�L|><��	�p^���UU��ƁI]�����x�;`,���,�-���9N�C]dSvRT��-x:(Э�(f��!*Κf06�2�:c 3�1�����('#�Z9��Qp��q�W�����؅Ei�aK1�	2v���s ���k"�0E���i��B�pX���:� ��1$秣ӏg������tuv��	Ĝ	$��𢪲N �����g��=I�v�]��UoϴG_��z&���&�AC�$�1����������/��?xB()QKCF�u1��\���yi��eI==|�VIi�&�,JWپ����Ѵ�^���d:�]�;m�ɓ�9�R�g���)4�M/+%R�pAH���m���u�ot��.zNo�����Q0�.�j�M�k�R��]v�k�Xw�I�X����kS�&�6��U@ ���H1 $g�����?
v����Q�h�k�p܍W7�nu�S�Wct;A�s����fGx:�����,є�3�
,�}�ɛD#d�,��H0^��c��6m��
R*-a&>�N�e5q�\O}� `<�xĕm&�ʦ98{��]�v'�7f���;����q���.���:�>b��d���{�׀�I�)�bPvk�̱��B�� ��H��ZI�H�\�mh�|�����k?dߛ["�3�ik�N�+��jW��-_4�q8�>�7ὧ6(�� �� AI��b{�@�ABSi��25��k���ɾѿ����{�ƚ��E���۶5���o��	�	�1��&Bk9�%}2������&�ktpp�䓍�     