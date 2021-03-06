# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(choices=[(1800, 1800), (1801, 1801), (1802, 1802), (1803, 1803), (1804, 1804), (1805, 1805), (1806, 1806), (1807, 1807), (1808, 1808), (1809, 1809), (1810, 1810), (1811, 1811), (1812, 1812), (1813, 1813), (1814, 1814), (1815, 1815), (1816, 1816), (1817, 1817), (1818, 1818), (1819, 1819), (1820, 1820), (1821, 1821), (1822, 1822), (1823, 1823), (1824, 1824), (1825, 1825), (1826, 1826), (1827, 1827), (1828, 1828), (1829, 1829), (1830, 1830), (1831, 1831), (1832, 1832), (1833, 1833), (1834, 1834), (1835, 1835), (1836, 1836), (1837, 1837), (1838, 1838), (1839, 1839), (1840, 1840), (1841, 1841), (1842, 1842), (1843, 1843), (1844, 1844), (1845, 1845), (1846, 1846), (1847, 1847), (1848, 1848), (1849, 1849), (1850, 1850), (1851, 1851), (1852, 1852), (1853, 1853), (1854, 1854), (1855, 1855), (1856, 1856), (1857, 1857), (1858, 1858), (1859, 1859), (1860, 1860), (1861, 1861), (1862, 1862), (1863, 1863), (1864, 1864), (1865, 1865), (1866, 1866), (1867, 1867), (1868, 1868), (1869, 1869), (1870, 1870), (1871, 1871), (1872, 1872), (1873, 1873), (1874, 1874), (1875, 1875), (1876, 1876), (1877, 1877), (1878, 1878), (1879, 1879), (1880, 1880), (1881, 1881), (1882, 1882), (1883, 1883), (1884, 1884), (1885, 1885), (1886, 1886), (1887, 1887), (1888, 1888), (1889, 1889), (1890, 1890), (1891, 1891), (1892, 1892), (1893, 1893), (1894, 1894), (1895, 1895), (1896, 1896), (1897, 1897), (1898, 1898), (1899, 1899), (1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100), (2101, 2101), (2102, 2102), (2103, 2103), (2104, 2104), (2105, 2105), (2106, 2106), (2107, 2107), (2108, 2108), (2109, 2109), (2110, 2110), (2111, 2111), (2112, 2112), (2113, 2113), (2114, 2114), (2115, 2115), (2116, 2116), (2117, 2117), (2118, 2118), (2119, 2119), (2120, 2120), (2121, 2121), (2122, 2122), (2123, 2123), (2124, 2124), (2125, 2125), (2126, 2126), (2127, 2127), (2128, 2128), (2129, 2129), (2130, 2130), (2131, 2131), (2132, 2132), (2133, 2133), (2134, 2134), (2135, 2135), (2136, 2136), (2137, 2137), (2138, 2138), (2139, 2139), (2140, 2140), (2141, 2141), (2142, 2142), (2143, 2143), (2144, 2144), (2145, 2145), (2146, 2146), (2147, 2147), (2148, 2148), (2149, 2149), (2150, 2150), (2151, 2151), (2152, 2152), (2153, 2153), (2154, 2154), (2155, 2155), (2156, 2156), (2157, 2157), (2158, 2158), (2159, 2159), (2160, 2160), (2161, 2161), (2162, 2162), (2163, 2163), (2164, 2164), (2165, 2165), (2166, 2166), (2167, 2167), (2168, 2168), (2169, 2169), (2170, 2170), (2171, 2171), (2172, 2172), (2173, 2173), (2174, 2174), (2175, 2175), (2176, 2176), (2177, 2177), (2178, 2178), (2179, 2179), (2180, 2180), (2181, 2181), (2182, 2182), (2183, 2183), (2184, 2184), (2185, 2185), (2186, 2186), (2187, 2187), (2188, 2188), (2189, 2189), (2190, 2190), (2191, 2191), (2192, 2192), (2193, 2193), (2194, 2194), (2195, 2195), (2196, 2196), (2197, 2197), (2198, 2198), (2199, 2199), (2200, 2200), (2201, 2201), (2202, 2202), (2203, 2203), (2204, 2204), (2205, 2205), (2206, 2206), (2207, 2207), (2208, 2208), (2209, 2209), (2210, 2210), (2211, 2211), (2212, 2212), (2213, 2213), (2214, 2214), (2215, 2215), (2216, 2216), (2217, 2217), (2218, 2218), (2219, 2219), (2220, 2220), (2221, 2221), (2222, 2222), (2223, 2223), (2224, 2224), (2225, 2225), (2226, 2226), (2227, 2227), (2228, 2228), (2229, 2229), (2230, 2230), (2231, 2231), (2232, 2232), (2233, 2233), (2234, 2234), (2235, 2235), (2236, 2236), (2237, 2237), (2238, 2238), (2239, 2239), (2240, 2240), (2241, 2241), (2242, 2242), (2243, 2243), (2244, 2244), (2245, 2245), (2246, 2246), (2247, 2247), (2248, 2248), (2249, 2249), (2250, 2250), (2251, 2251), (2252, 2252), (2253, 2253), (2254, 2254), (2255, 2255), (2256, 2256), (2257, 2257), (2258, 2258), (2259, 2259), (2260, 2260), (2261, 2261), (2262, 2262), (2263, 2263), (2264, 2264), (2265, 2265), (2266, 2266), (2267, 2267), (2268, 2268), (2269, 2269), (2270, 2270), (2271, 2271), (2272, 2272), (2273, 2273), (2274, 2274), (2275, 2275), (2276, 2276), (2277, 2277), (2278, 2278), (2279, 2279), (2280, 2280), (2281, 2281), (2282, 2282), (2283, 2283), (2284, 2284), (2285, 2285), (2286, 2286), (2287, 2287), (2288, 2288), (2289, 2289), (2290, 2290), (2291, 2291), (2292, 2292), (2293, 2293), (2294, 2294), (2295, 2295), (2296, 2296), (2297, 2297), (2298, 2298), (2299, 2299), (2300, 2300), (2301, 2301), (2302, 2302), (2303, 2303), (2304, 2304), (2305, 2305), (2306, 2306), (2307, 2307), (2308, 2308), (2309, 2309), (2310, 2310), (2311, 2311), (2312, 2312), (2313, 2313), (2314, 2314), (2315, 2315), (2316, 2316), (2317, 2317), (2318, 2318), (2319, 2319), (2320, 2320), (2321, 2321), (2322, 2322), (2323, 2323), (2324, 2324), (2325, 2325), (2326, 2326), (2327, 2327), (2328, 2328), (2329, 2329), (2330, 2330), (2331, 2331), (2332, 2332), (2333, 2333), (2334, 2334), (2335, 2335), (2336, 2336), (2337, 2337), (2338, 2338), (2339, 2339), (2340, 2340), (2341, 2341), (2342, 2342), (2343, 2343), (2344, 2344), (2345, 2345), (2346, 2346), (2347, 2347), (2348, 2348), (2349, 2349), (2350, 2350), (2351, 2351), (2352, 2352), (2353, 2353), (2354, 2354), (2355, 2355), (2356, 2356), (2357, 2357), (2358, 2358), (2359, 2359), (2360, 2360), (2361, 2361), (2362, 2362), (2363, 2363), (2364, 2364), (2365, 2365), (2366, 2366), (2367, 2367), (2368, 2368), (2369, 2369), (2370, 2370), (2371, 2371), (2372, 2372), (2373, 2373), (2374, 2374), (2375, 2375), (2376, 2376), (2377, 2377), (2378, 2378), (2379, 2379), (2380, 2380), (2381, 2381), (2382, 2382), (2383, 2383), (2384, 2384), (2385, 2385), (2386, 2386), (2387, 2387), (2388, 2388), (2389, 2389), (2390, 2390), (2391, 2391), (2392, 2392), (2393, 2393), (2394, 2394), (2395, 2395), (2396, 2396), (2397, 2397), (2398, 2398), (2399, 2399), (2400, 2400), (2401, 2401), (2402, 2402), (2403, 2403), (2404, 2404), (2405, 2405), (2406, 2406), (2407, 2407), (2408, 2408), (2409, 2409), (2410, 2410), (2411, 2411), (2412, 2412), (2413, 2413), (2414, 2414), (2415, 2415), (2416, 2416), (2417, 2417), (2418, 2418), (2419, 2419), (2420, 2420), (2421, 2421), (2422, 2422), (2423, 2423), (2424, 2424), (2425, 2425), (2426, 2426), (2427, 2427), (2428, 2428), (2429, 2429), (2430, 2430), (2431, 2431), (2432, 2432), (2433, 2433), (2434, 2434), (2435, 2435), (2436, 2436), (2437, 2437), (2438, 2438), (2439, 2439), (2440, 2440), (2441, 2441), (2442, 2442), (2443, 2443), (2444, 2444), (2445, 2445), (2446, 2446), (2447, 2447), (2448, 2448), (2449, 2449), (2450, 2450), (2451, 2451), (2452, 2452), (2453, 2453), (2454, 2454), (2455, 2455), (2456, 2456), (2457, 2457), (2458, 2458), (2459, 2459), (2460, 2460), (2461, 2461), (2462, 2462), (2463, 2463), (2464, 2464), (2465, 2465), (2466, 2466), (2467, 2467), (2468, 2468), (2469, 2469), (2470, 2470), (2471, 2471), (2472, 2472), (2473, 2473), (2474, 2474), (2475, 2475), (2476, 2476), (2477, 2477), (2478, 2478), (2479, 2479), (2480, 2480), (2481, 2481), (2482, 2482), (2483, 2483), (2484, 2484), (2485, 2485), (2486, 2486), (2487, 2487), (2488, 2488), (2489, 2489), (2490, 2490), (2491, 2491), (2492, 2492), (2493, 2493), (2494, 2494), (2495, 2495), (2496, 2496), (2497, 2497), (2498, 2498), (2499, 2499), (2500, 2500)])),
            ],
        ),
        migrations.CreateModel(
            name='GoalScored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=255)),
                ('kickoff', models.DateTimeField(help_text='UTC Time')),
                ('home_score', models.IntegerField(null=True)),
                ('away_score', models.IntegerField(null=True)),
                ('home_penalty_score', models.IntegerField(blank=True, null=True)),
                ('away_penalty_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.DateField()),
                ('height', models.IntegerField(blank=True, help_text='height in cm', null=True)),
                ('position', models.CharField(choices=[('GK', 'Goalkeeper'), ('D', 'Defender'), ('LB', 'Left Back'), ('CB', 'Center Back'), ('RB', 'Right Back'), ('M', 'Midfielder'), ('LM', 'Left Midfielder'), ('CM', 'Center Midfielder'), ('RM', 'Right Midfielder'), ('F', 'Forward'), ('LF', 'Left Forward'), ('CF', 'Center Forward'), ('RF', 'Right Forward')], max_length=3)),
                ('number', models.IntegerField(blank=True, help_text='Number most often worn', null=True)),
                ('country', models.CharField(max_length=255)),
                ('country_2', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('caps', models.IntegerField(default=0)),
                ('twitter_handle', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_handle', models.CharField(blank=True, max_length=255, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('wikipedia', models.URLField(blank=True, null=True)),
                ('fun_facts', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_played', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.IntegerField(choices=[(1, 'National'), (2, 'League')])),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('country', models.CharField(max_length=255)),
                ('stadium', models.CharField(blank=True, max_length=255, null=True)),
                ('year_started', models.IntegerField(choices=[(1800, 1800), (1801, 1801), (1802, 1802), (1803, 1803), (1804, 1804), (1805, 1805), (1806, 1806), (1807, 1807), (1808, 1808), (1809, 1809), (1810, 1810), (1811, 1811), (1812, 1812), (1813, 1813), (1814, 1814), (1815, 1815), (1816, 1816), (1817, 1817), (1818, 1818), (1819, 1819), (1820, 1820), (1821, 1821), (1822, 1822), (1823, 1823), (1824, 1824), (1825, 1825), (1826, 1826), (1827, 1827), (1828, 1828), (1829, 1829), (1830, 1830), (1831, 1831), (1832, 1832), (1833, 1833), (1834, 1834), (1835, 1835), (1836, 1836), (1837, 1837), (1838, 1838), (1839, 1839), (1840, 1840), (1841, 1841), (1842, 1842), (1843, 1843), (1844, 1844), (1845, 1845), (1846, 1846), (1847, 1847), (1848, 1848), (1849, 1849), (1850, 1850), (1851, 1851), (1852, 1852), (1853, 1853), (1854, 1854), (1855, 1855), (1856, 1856), (1857, 1857), (1858, 1858), (1859, 1859), (1860, 1860), (1861, 1861), (1862, 1862), (1863, 1863), (1864, 1864), (1865, 1865), (1866, 1866), (1867, 1867), (1868, 1868), (1869, 1869), (1870, 1870), (1871, 1871), (1872, 1872), (1873, 1873), (1874, 1874), (1875, 1875), (1876, 1876), (1877, 1877), (1878, 1878), (1879, 1879), (1880, 1880), (1881, 1881), (1882, 1882), (1883, 1883), (1884, 1884), (1885, 1885), (1886, 1886), (1887, 1887), (1888, 1888), (1889, 1889), (1890, 1890), (1891, 1891), (1892, 1892), (1893, 1893), (1894, 1894), (1895, 1895), (1896, 1896), (1897, 1897), (1898, 1898), (1899, 1899), (1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100), (2101, 2101), (2102, 2102), (2103, 2103), (2104, 2104), (2105, 2105), (2106, 2106), (2107, 2107), (2108, 2108), (2109, 2109), (2110, 2110), (2111, 2111), (2112, 2112), (2113, 2113), (2114, 2114), (2115, 2115), (2116, 2116), (2117, 2117), (2118, 2118), (2119, 2119), (2120, 2120), (2121, 2121), (2122, 2122), (2123, 2123), (2124, 2124), (2125, 2125), (2126, 2126), (2127, 2127), (2128, 2128), (2129, 2129), (2130, 2130), (2131, 2131), (2132, 2132), (2133, 2133), (2134, 2134), (2135, 2135), (2136, 2136), (2137, 2137), (2138, 2138), (2139, 2139), (2140, 2140), (2141, 2141), (2142, 2142), (2143, 2143), (2144, 2144), (2145, 2145), (2146, 2146), (2147, 2147), (2148, 2148), (2149, 2149), (2150, 2150), (2151, 2151), (2152, 2152), (2153, 2153), (2154, 2154), (2155, 2155), (2156, 2156), (2157, 2157), (2158, 2158), (2159, 2159), (2160, 2160), (2161, 2161), (2162, 2162), (2163, 2163), (2164, 2164), (2165, 2165), (2166, 2166), (2167, 2167), (2168, 2168), (2169, 2169), (2170, 2170), (2171, 2171), (2172, 2172), (2173, 2173), (2174, 2174), (2175, 2175), (2176, 2176), (2177, 2177), (2178, 2178), (2179, 2179), (2180, 2180), (2181, 2181), (2182, 2182), (2183, 2183), (2184, 2184), (2185, 2185), (2186, 2186), (2187, 2187), (2188, 2188), (2189, 2189), (2190, 2190), (2191, 2191), (2192, 2192), (2193, 2193), (2194, 2194), (2195, 2195), (2196, 2196), (2197, 2197), (2198, 2198), (2199, 2199), (2200, 2200), (2201, 2201), (2202, 2202), (2203, 2203), (2204, 2204), (2205, 2205), (2206, 2206), (2207, 2207), (2208, 2208), (2209, 2209), (2210, 2210), (2211, 2211), (2212, 2212), (2213, 2213), (2214, 2214), (2215, 2215), (2216, 2216), (2217, 2217), (2218, 2218), (2219, 2219), (2220, 2220), (2221, 2221), (2222, 2222), (2223, 2223), (2224, 2224), (2225, 2225), (2226, 2226), (2227, 2227), (2228, 2228), (2229, 2229), (2230, 2230), (2231, 2231), (2232, 2232), (2233, 2233), (2234, 2234), (2235, 2235), (2236, 2236), (2237, 2237), (2238, 2238), (2239, 2239), (2240, 2240), (2241, 2241), (2242, 2242), (2243, 2243), (2244, 2244), (2245, 2245), (2246, 2246), (2247, 2247), (2248, 2248), (2249, 2249), (2250, 2250), (2251, 2251), (2252, 2252), (2253, 2253), (2254, 2254), (2255, 2255), (2256, 2256), (2257, 2257), (2258, 2258), (2259, 2259), (2260, 2260), (2261, 2261), (2262, 2262), (2263, 2263), (2264, 2264), (2265, 2265), (2266, 2266), (2267, 2267), (2268, 2268), (2269, 2269), (2270, 2270), (2271, 2271), (2272, 2272), (2273, 2273), (2274, 2274), (2275, 2275), (2276, 2276), (2277, 2277), (2278, 2278), (2279, 2279), (2280, 2280), (2281, 2281), (2282, 2282), (2283, 2283), (2284, 2284), (2285, 2285), (2286, 2286), (2287, 2287), (2288, 2288), (2289, 2289), (2290, 2290), (2291, 2291), (2292, 2292), (2293, 2293), (2294, 2294), (2295, 2295), (2296, 2296), (2297, 2297), (2298, 2298), (2299, 2299), (2300, 2300), (2301, 2301), (2302, 2302), (2303, 2303), (2304, 2304), (2305, 2305), (2306, 2306), (2307, 2307), (2308, 2308), (2309, 2309), (2310, 2310), (2311, 2311), (2312, 2312), (2313, 2313), (2314, 2314), (2315, 2315), (2316, 2316), (2317, 2317), (2318, 2318), (2319, 2319), (2320, 2320), (2321, 2321), (2322, 2322), (2323, 2323), (2324, 2324), (2325, 2325), (2326, 2326), (2327, 2327), (2328, 2328), (2329, 2329), (2330, 2330), (2331, 2331), (2332, 2332), (2333, 2333), (2334, 2334), (2335, 2335), (2336, 2336), (2337, 2337), (2338, 2338), (2339, 2339), (2340, 2340), (2341, 2341), (2342, 2342), (2343, 2343), (2344, 2344), (2345, 2345), (2346, 2346), (2347, 2347), (2348, 2348), (2349, 2349), (2350, 2350), (2351, 2351), (2352, 2352), (2353, 2353), (2354, 2354), (2355, 2355), (2356, 2356), (2357, 2357), (2358, 2358), (2359, 2359), (2360, 2360), (2361, 2361), (2362, 2362), (2363, 2363), (2364, 2364), (2365, 2365), (2366, 2366), (2367, 2367), (2368, 2368), (2369, 2369), (2370, 2370), (2371, 2371), (2372, 2372), (2373, 2373), (2374, 2374), (2375, 2375), (2376, 2376), (2377, 2377), (2378, 2378), (2379, 2379), (2380, 2380), (2381, 2381), (2382, 2382), (2383, 2383), (2384, 2384), (2385, 2385), (2386, 2386), (2387, 2387), (2388, 2388), (2389, 2389), (2390, 2390), (2391, 2391), (2392, 2392), (2393, 2393), (2394, 2394), (2395, 2395), (2396, 2396), (2397, 2397), (2398, 2398), (2399, 2399), (2400, 2400), (2401, 2401), (2402, 2402), (2403, 2403), (2404, 2404), (2405, 2405), (2406, 2406), (2407, 2407), (2408, 2408), (2409, 2409), (2410, 2410), (2411, 2411), (2412, 2412), (2413, 2413), (2414, 2414), (2415, 2415), (2416, 2416), (2417, 2417), (2418, 2418), (2419, 2419), (2420, 2420), (2421, 2421), (2422, 2422), (2423, 2423), (2424, 2424), (2425, 2425), (2426, 2426), (2427, 2427), (2428, 2428), (2429, 2429), (2430, 2430), (2431, 2431), (2432, 2432), (2433, 2433), (2434, 2434), (2435, 2435), (2436, 2436), (2437, 2437), (2438, 2438), (2439, 2439), (2440, 2440), (2441, 2441), (2442, 2442), (2443, 2443), (2444, 2444), (2445, 2445), (2446, 2446), (2447, 2447), (2448, 2448), (2449, 2449), (2450, 2450), (2451, 2451), (2452, 2452), (2453, 2453), (2454, 2454), (2455, 2455), (2456, 2456), (2457, 2457), (2458, 2458), (2459, 2459), (2460, 2460), (2461, 2461), (2462, 2462), (2463, 2463), (2464, 2464), (2465, 2465), (2466, 2466), (2467, 2467), (2468, 2468), (2469, 2469), (2470, 2470), (2471, 2471), (2472, 2472), (2473, 2473), (2474, 2474), (2475, 2475), (2476, 2476), (2477, 2477), (2478, 2478), (2479, 2479), (2480, 2480), (2481, 2481), (2482, 2482), (2483, 2483), (2484, 2484), (2485, 2485), (2486, 2486), (2487, 2487), (2488, 2488), (2489, 2489), (2490, 2490), (2491, 2491), (2492, 2492), (2493, 2493), (2494, 2494), (2495, 2495), (2496, 2496), (2497, 2497), (2498, 2498), (2499, 2499), (2500, 2500)])),
                ('active', models.BooleanField(default=True)),
                ('previous_name', models.CharField(blank=True, max_length=255, null=True)),
                ('coach', models.CharField(max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('league', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soccer.League')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayerRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=True)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Player')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soccer.Team')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCareerStatistics',
            fields=[
                ('statistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.Statistics')),
                ('minutes_played', models.IntegerField()),
                ('yellow_cards', models.IntegerField(help_text='Usually abbreviated as YC')),
                ('red_cards', models.IntegerField(help_text='Usually abbreviated as RC')),
            ],
            bases=('soccer.statistics',),
        ),
        migrations.CreateModel(
            name='TeamAllTimeStatistics',
            fields=[
                ('statistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.Statistics')),
                ('goals_for', models.IntegerField(help_text='Usually abbreviated as F')),
                ('goals_against', models.IntegerField(help_text='Usually abbreviated as A')),
                ('goal_difference', models.IntegerField(help_text='Usually abbreviated as GD')),
                ('points', models.IntegerField()),
            ],
            bases=('soccer.statistics',),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='away_matches', to='soccer.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Competition'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='home_matches', to='soccer.Team'),
        ),
        migrations.AddField(
            model_name='goalscored',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Match'),
        ),
        migrations.AddField(
            model_name='goalscored',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='soccer.Player'),
        ),
        migrations.AddField(
            model_name='competition',
            name='champion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='competition_won', to='soccer.Team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='league',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soccer.League'),
        ),
        migrations.AddField(
            model_name='competition',
            name='participants',
            field=models.ManyToManyField(related_name='competition_participated', to='soccer.Team'),
        ),
        migrations.CreateModel(
            name='GoalkeeperCareerStatistics',
            fields=[
                ('playercareerstatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.PlayerCareerStatistics')),
                ('saves', models.IntegerField(help_text='Usually abbreviated as SV')),
                ('goals_allowed', models.IntegerField(help_text='Usually abbreviated as GA')),
                ('shots_on_goal_against', models.IntegerField(help_text='Usually abbreviated as SOG')),
                ('shots_against', models.IntegerField(help_text='Usually abbreviated as S')),
                ('clean_sheets', models.IntegerField(help_text='Usually abbreviated as CS')),
            ],
            bases=('soccer.playercareerstatistics',),
        ),
        migrations.CreateModel(
            name='OutfieldPlayerCareerStatistics',
            fields=[
                ('playercareerstatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.PlayerCareerStatistics')),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField(help_text='Usually abbreviated as A')),
                ('shots_on_goal', models.IntegerField(help_text='Usually abbreviated as SG. Sometimes called shots on target.')),
                ('shots', models.IntegerField(help_text='Usually abbreviated as SH.')),
            ],
            bases=('soccer.playercareerstatistics',),
        ),
        migrations.CreateModel(
            name='TeamCompetitionStatistics',
            fields=[
                ('teamalltimestatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.TeamAllTimeStatistics')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Competition')),
            ],
            bases=('soccer.teamalltimestatistics',),
        ),
        migrations.AddField(
            model_name='teamalltimestatistics',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='soccer.Team'),
        ),
        migrations.AddField(
            model_name='playercareerstatistics',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='soccer.Player'),
        ),
        migrations.CreateModel(
            name='GoalkeeperCompetitionStatistics',
            fields=[
                ('goalkeepercareerstatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.GoalkeeperCareerStatistics')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Competition')),
            ],
            bases=('soccer.goalkeepercareerstatistics',),
        ),
        migrations.CreateModel(
            name='OutfieldPlayerCompetitionStatistics',
            fields=[
                ('outfieldplayercareerstatistics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='soccer.OutfieldPlayerCareerStatistics')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.Competition')),
            ],
            bases=('soccer.outfieldplayercareerstatistics',),
        ),
    ]
