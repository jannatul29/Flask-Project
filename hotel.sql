PGDMP     :    &                 z            store    14.1    14.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16400    store    DATABASE     i   CREATE DATABASE store WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE store;
                postgres    false            �            1259    24665    hotel    TABLE     �   CREATE TABLE public.hotel (
    id integer NOT NULL,
    title character varying,
    herf character varying,
    image character varying,
    rating character varying,
    price character varying,
    location character varying,
    amenities text
);
    DROP TABLE public.hotel;
       public         heap    postgres    false            �            1259    24664    test12_id_seq    SEQUENCE     �   CREATE SEQUENCE public.test12_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.test12_id_seq;
       public          postgres    false    220                       0    0    test12_id_seq    SEQUENCE OWNED BY     >   ALTER SEQUENCE public.test12_id_seq OWNED BY public.hotel.id;
          public          postgres    false    219            �           2604    24668    hotel id    DEFAULT     e   ALTER TABLE ONLY public.hotel ALTER COLUMN id SET DEFAULT nextval('public.test12_id_seq'::regclass);
 7   ALTER TABLE public.hotel ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220                      0    24665    hotel 
   TABLE DATA           [   COPY public.hotel (id, title, herf, image, rating, price, location, amenities) FROM stdin;
    public          postgres    false    220   �
                  0    0    test12_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.test12_id_seq', 33, true);
          public          postgres    false    219            �           2606    24672    hotel hotel_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.hotel DROP CONSTRAINT hotel_pkey;
       public            postgres    false    220                 x��V�n�F}v��O'�xn�[��J9������V�U4��b�����_���k?�_��%@�@f�x����&4��M8�O�:ȝ�/��p�ZES���(����f�ו3����]a,����fgZYg��j�f6�����M`�|�4�Ej���0 0G�"�H��s%y��|����\~F)���b��3�姴��g�^�@Eqx�Gj�ҟ���?��-?	�[��8|07+�:�z|Y>�8>�着l���06+���h��;"qp��ixW�?�.N�C]dvR�TZ(�:(Э�(f��}T�6���@�ʘ���tl�*�G9����N�=K�˿�V�F.�*J�[�!8L����; �|�[�&"S����*	������
�C�	��|p�������OË��A̙@�)���*��Xz��Yfl�Փ�/���:lzc華�v�?��yw��?z>���� �� h#)RhњB&g��T��L�D�t\y�w�*�%�����Z�J�o+��^��C����R�����ڧ��AC�8��{�#.|!����/���?��
��D-Q����R�K�ӓ��j����5Y��E�*���aǣ	��̾�t�[�w�T����J�Qt�O�1P�m�zY}���Dq�T�������.��.1ۆe��]l@�j�����/��b좰��F0Ѐ�=�/قE�a��ybc
���I�
��)�b��=G ٍ ��b{^�mr�F�vE��tu��N�:55F�t;7́��h��}��
�%�$���(W�w�B�e'o���=f������&�,�{�i3�|��}8i	3uu��j슙������t�����K�����c�vͷ�0rܚU�go������XS{��Xn�=�$>k���#����jL��Z�cIE��x7��v"��ϔ�\�I]��n\��:;=�r���]���`mx���b�٬Ld��FB�Q�����]D)�iɫ�%���Z�|��>x.�5:::�_돏     