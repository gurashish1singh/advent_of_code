from __future__ import annotations

INPUT_STRING_1 = """
1429
1368
1661
1687
1593
1495
1565
1500
1635
1845
1645
1999
1415
1054
1930
1774
1405
1993
1757
1623
1675
1665
631
1950
1702
1311
1509
1790
1643
1884
226
1455
1679
1746
1284
1342
1684
1543
1396
1806
1523
1363
1011
1577
1767
1287
1885
1517
1556
1722
1260
1624
1466
1263
1162
1688
1202
1913
1964
1385
1970
1976
1431
858
1748
1544
1438
1300
1926
1587
1376
1939
1039
1639
1539
1491
1631
1521
1564
1507
1637
1534
1713
1533
1118
1356
2003
282
1079
1837
1259
1941
1836
1903
1433
1467
1027
1441
1048
1742
1087
1872
1476
1657
1361
1182
1494
1529
1822
1444
1330
1514
1723
1432
1683
1997
1443
1474
1932
1504
1313
1765
19
1784
1619
992
1560
1680
1626
1558
1899
1293
1676
1161
1140
1341
1597
1628
1611
1302
1269
1241
1952
1591
1726
428
1703
1289
1109
1478
1002
1817
1849
1838
1319
1641
583
1920
1453
1411
1870
1763
1469
1646
1719
1213
1462
1545
1682
1711
18
2004
1252
1620
1559
1315
781
1656
1987
1436
1630
1985
1897
1551
1296
1282
1735
1320
1659
1271
1380
1274
1876
1492
1298
1399
1692
1265
1555
1337
"""
INPUT_STRING_2 = """
"5-11 t: glhbttzvzttkdx"
"2-4 f: cfkmf"
"9-12 m: mmmmmmmmmmmmm"
"2-10 z: vghqbzbcxf"
"10-11 b: tbtbvbbnbwd"
"1-6 d: cmhdnw"
"1-5 r: xrrrdrrr"
"12-13 g: pggkggggfggggg"
"7-9 g: gsgwhgggg"
"4-5 v: tvsgqvvv"
"5-7 n: nnncngdnznjx"
"1-4 v: vvvzqvzvvvvv"
"11-12 r: mmrwxhrzvmrr"
"5-11 f: wcldfbbkxbfjrtffrr"
"3-4 x: pcnxgxx"
"11-12 g: kgggghpfgmwzgg"
"2-3 z: zzzzmzn"
"11-12 n: nrncpbpnlpnn"
"2-4 q: qqgq"
"11-14 k: kkkkkkkkkkkkkkk"
"4-10 w: fkswkgwwhpjfcg"
"6-12 s: sssshsssfssw"
"2-14 d: szcsdskhhqrpldwp"
"1-5 j: zjpjjqxjjjrjjjj"
"9-13 q: qqqqqqlqjqwqhqqr"
"1-9 f: vrffffffxffnfbffff"
"13-14 s: ssssssssssssskm"
"3-6 z: mwrzcnnf"
"8-9 c: bccczcccctjv"
"2-4 j: hxpd"
"8-12 w: fwvzwgfwdwxww"
"3-12 h: hhtmhhphrhhbhhhk"
"2-4 r: hrqr"
"10-11 f: ffffqfffhflfffffff"
"2-6 j: ggppjc"
"8-16 l: cltwcjcsxllxctxs"
"3-4 t: ttwj"
"10-12 b: bqbcbqlnzbtbrm"
"12-13 l: llllslllwlllgltdlll"
"4-7 x: xfvxbqxs"
"5-6 v: xrvqvv"
"11-17 q: mdblqqptcvqqfqqqq"
"8-19 f: ffpdzwvcffmsffffbffl"
"12-14 w: hwpjcxgcvpwhww"
"2-4 d: pzdtd"
"9-10 p: vgtpmmxppp"
"3-4 k: vkwh"
"14-15 d: swgpzprkmrkxdddk"
"13-14 z: gxzzgzzjhlzzzs"
"4-5 b: bbgbbp"
"2-4 p: pnqcn"
"16-20 d: rkqpfvbfvtcgdmhddpdd"
"2-3 l: llzpllll"
"6-10 v: hdnxdvxmxv"
"2-4 m: xcfmcmmmzgw"
"9-12 n: fmcndbqvnlnncqnxffmz"
"3-12 t: bcttczggbtgt"
"4-6 j: vwvjlq"
"4-5 t: mttfttvtttttttw"
"3-5 v: vxjvq"
"5-7 z: kzvzzrzmwwxtnsrmhp"
"9-11 p: ppppppppppppppppp"
"5-7 n: nbzdpqvxxcmn"
"5-6 n: cnnntn"
"2-7 r: rrrrrrrrhrrwrrrr"
"6-18 s: stngssgssnsrsflsssk"
"11-14 q: qqqqqqqqqqqqqnq"
"3-5 d: dtdvd"
"3-4 m: mmqn"
"7-10 d: ddddddddddd"
"7-11 k: kkkkkkkckkkkk"
"9-16 z: zzxzgwtjzzzzzhkz"
"6-8 l: lllllllll"
"13-18 z: tszsszrlzzqzzkzwxjxd"
"3-11 b: bbcbbbbnbbppbbb"
"2-8 j: jjjjjjjjjjjjjpjjjj"
"1-8 f: fcltvbhffbqf"
"6-19 m: hhvkzmqtmpvbvrbhwmm"
"7-8 z: qzzmzzzzqz"
"2-5 b: fhbwb"
"3-4 m: mrlqtlkphwnc"
"8-10 p: cprpgpwkpp"
"2-5 t: tttttt"
"7-10 m: zlrbpxxwvrjxs"
"10-14 q: gddtnqqcqlfqshq"
"9-11 p: kpzpppppnhspp"
"1-5 n: wfvnv"
"7-8 k: fbzwwdkdx"
"2-5 d: gjgxfdcvhrmwwrl"
"1-3 s: sxss"
"8-12 n: nnnnnnnsnnnnnncvnn"
"11-12 c: cccccccccccvc"
"3-10 v: bvvvvgwdvqbv"
"6-15 b: hfnlwhxxmbgwbbkgfp"
"18-19 m: mbfbmmjmmmmvmmjcpmc"
"1-13 n: jxbqfntqxwjncfzmftjv"
"3-5 b: rqxpblz"
"14-16 n: nnnbpnnpgnptnsnhnnn"
"8-9 g: jgzgfgpqq"
"9-10 f: fffffffffff"
"5-7 c: crcctccc"
"5-9 j: nnkwgjtjj"
"5-7 f: mxffbff"
"2-4 g: qggng"
"4-8 r: rxrrzpjrmqlgvkv"
"8-17 q: wqtdqqqkqqlldqqqfrq"
"10-11 h: spmxjhhhhhh"
"3-4 q: qqkq"
"4-6 b: bbbbkb"
"15-16 x: xxxxxxfxxxxvxxfxxx"
"3-4 k: kqxm"
"4-9 w: cbkrrgkzg"
"14-17 s: sssssssssssssdssms"
"17-18 c: cccccccccccccccckccc"
"6-8 l: llllmgllkqsllsq"
"16-19 k: kkkkkkkkkkkkkkkkkkgk"
"15-17 f: ffqffffffffffffff"
"16-19 p: pppppppppppppppgpppp"
"1-2 s: ssnsl"
"5-17 v: vgwwvvfvvldvsqqwvgt"
"5-7 m: mtbqmfm"
"3-6 b: wmzbxbxx"
"9-19 h: lhmwjzxchvjsxtmbmqh"
"10-11 p: ppppppppppzpp"
"3-16 p: ppqppppppppppppppjpp"
"3-4 p: hpjhhw"
"8-12 m: wzvmhjnmlbdmwlnvwwh"
"4-7 n: nnnnnnhnnn"
"11-13 h: hhchrhthhmhhcmg"
"1-4 f: fffh"
"6-8 q: qqqqqqqq"
"4-12 d: dddddddddddkd"
"2-8 g: gkgggggrqggg"
"12-18 g: ggjhbbljhgtfrgwgggg"
"5-15 d: dddddddddddddddd"
"7-12 v: kkmcjvvvvhvvpv"
"3-11 r: nhrcwzxhrsr"
"6-8 h: dhhhnhzhhdhhh"
"2-3 k: vfkckkk"
"3-18 c: nxcrgvbbchzbznxqxb"
"3-6 x: xxxxxxxx"
"11-15 w: wwwwwwwwlwlwxwwkh"
"7-12 t: jttttwdtkzttttft"
"6-7 l: tqslglhkxmcmjksxlc"
"1-4 s: kssz"
"14-16 b: bbbbbbtbbbbbbcbsbwbb"
"5-8 l: llllrllhll"
"6-7 d: bjddgkztz"
"4-5 x: cnxxtxxz"
"3-4 m: mmzdgmtmwm"
"2-6 z: zzzzzhlzz"
"9-14 b: jhbbkdpfwrvbsqchgl"
"8-14 q: wqbtbjpfxxwrgnp"
"14-19 p: pxmfpcpkppppprppcwx"
"5-8 w: wkcqvdwp"
"7-15 x: zwpzjkjtdrhlwksxdz"
"1-2 g: bggg"
"3-5 z: zzzzzzz"
"7-10 v: tvvvvvvpvvvvvvvv"
"2-3 r: rrrrrr"
"4-9 z: zpzmzzzzpzzp"
"4-6 s: dsnswc"
"1-12 f: fffzffffffffff"
"1-5 c: cqccvccczmccc"
"5-19 x: lgrsxhlwzthdxtwfbvx"
"3-10 t: xvhtznxhvgpx"
"3-11 x: gvhxpjmwxtxmgqks"
"11-13 b: rjvtlmntzpbbjprtlbb"
"1-4 m: mmmm"
"5-10 k: pkkgkkmnhk"
"2-3 v: vvmv"
"12-13 p: mppspppbfpgwp"
"1-3 m: mmmpmmbm"
"4-9 b: hzbjdbjxpxqbtlm"
"1-4 p: ppppppppppppppp"
"4-5 g: ggfgg"
"8-11 j: dwjzgmgdcczhwc"
"6-7 w: wwwwwwwww"
"3-5 t: vtqwt"
"1-5 k: kkhkkk"
"4-7 c: ccvtcrcc"
"1-10 l: vwknprttll"
"9-11 x: htnnvnrtxdx"
"15-17 r: rrrrxrrlrrrrrcrrs"
"2-3 v: vsvvv"
"4-15 g: mxjglqklwwjnksg"
"1-2 c: ccdc"
"10-16 l: ljrrlvtlrqglmgdf"
"3-6 s: ssssblsdsb"
"5-6 r: mrrrrtrr"
"13-17 w: wwwwghwwtkwwrwwfx"
"4-5 j: jjdjjzjjb"
"2-3 s: ssjsss"
"8-14 r: rrrrrrrrrrrrrrrrrr"
"7-9 l: lllllllllll"
"15-17 j: jjxjjjjjsjjjjjjjjjj"
"6-8 r: hrrrcqrr"
"6-7 w: wndbtqqmdw"
"4-7 k: cktskgxmkk"
"3-9 z: blkmxrzjhcp"
"10-11 p: ppppppzpfmpt"
"8-9 s: sssssssss"
"1-5 l: zglfs"
"7-8 s: mstsxsvsm"
"1-4 z: zzzzrbvzwr"
"16-17 g: ggggkgggggggggggggg"
"1-2 j: jjjjjwjjzj"
"4-18 m: zmmbvvsrcmmcmqmpwlm"
"11-15 f: ffffffffffvfffq"
"5-6 c: csvcccccc"
"1-12 z: zzzzzgzzzzzbqz"
"17-18 s: sssssssssssssssjns"
"6-10 m: jmfztgfmml"
"5-7 x: bnxxxrx"
"13-16 p: ppppppppppppmpphp"
"11-14 t: ttttttltttvttttx"
"13-14 t: qttnscscgxttttt"
"4-5 b: vzbhz"
"4-7 r: tdrzrrfqrrrrrrb"
"15-17 p: pppppppppppppppppp"
"9-17 q: xgqqnxppgqjqsbqqqdnv"
"3-15 t: hrrnrspnpkwcktg"
"3-6 f: fffcxf"
"3-8 n: nznvppnn"
"4-6 z: lzksskczzjzz"
"6-12 n: nnnnnsnnnnnwrn"
"11-12 q: qqnqqqpqqqcqqqqs"
"5-11 z: zzzzlzzzzzrzz"
"1-5 z: zzzzz"
"4-5 j: bsspj"
"18-19 d: ptdpdjpsdpddhsddkwd"
"13-16 k: kkkkkkkkkkkkfkkw"
"7-9 s: zsssbssfs"
"15-19 b: bbbbbbbbbbbbbbbbbbbb"
"1-7 g: gngrmgb"
"1-7 f: vgkmsrfgwlwqzvfk"
"7-11 p: psfkppdwxdt"
"1-12 p: hppbpppppppbpppppp"
"12-13 d: xxzpkwgzcxddq"
"6-7 k: ktkkkqk"
"8-9 v: vvvvvvvvvfvv"
"9-13 g: ggggggggggggzggg"
"6-7 g: gggggggggggggggggg"
"6-10 g: gqgggcgggf"
"3-9 r: wdkkqwbrgpvnrmvqc"
"2-4 x: xxsxjndqbd"
"13-14 j: jjjjmjjsjjjjjj"
"12-13 d: dddddddddddddd"
"3-4 h: rqnbzh"
"2-3 f: ftxhlhhpvdvnz"
"11-17 g: hnkmggstgggbgvrggj"
"6-7 c: cccccvc"
"3-4 m: mmtm"
"2-7 r: rhrrrrr"
"6-14 l: wpzllljvxdsxblz"
"7-8 b: wxbrbbbb"
"9-12 q: qfqqqqqqlqqrqvq"
"11-15 p: ppppppppppppppppppp"
"19-20 l: vjbsvzclllslkmlslxml"
"4-5 v: jvnbhkv"
"12-16 j: jfjjjjjjjkjsjjjvjjj"
"3-4 w: wwww"
"1-4 v: kvnv"
"1-5 r: hrrrdrrrrrrrrrrrr"
"18-19 s: skwfsfqfmhfgkbsmsnj"
"3-4 f: pfks"
"11-12 p: ttpbsjfvxcdm"
"4-8 d: vhdddgndrmddfdg"
"1-3 j: sbjwgvvhvj"
"13-20 l: gslclvrnllgljtljmlnn"
"9-11 m: mmmmmmmjkmdrmmmm"
"8-14 r: fmzrhrdssfmxkq"
"3-9 f: rvfmskmdfk"
"3-13 c: ccjcccccccccbc"
"15-16 w: wwwwwwwwwwwwwwwww"
"4-5 r: hrlnjk"
"5-13 q: qqqqqqqqqqqqqqqq"
"15-16 j: jjjjjjjjjjjjjjjjj"
"18-19 p: mhsgkktbhpwvvqmppbmc"
"13-15 g: vfjtrgrrkbstblz"
"12-15 j: jjjjkczjjjjjjpjjjvjx"
"3-4 b: dbbb"
"6-7 s: sbssskssss"
"15-16 p: jgppppsspppppgxwm"
"2-11 f: hmhwwqcjdfk"
"4-6 t: tttttqt"
"1-8 r: vrrrrdqrrrrrrrrrrr"
"2-5 v: lftqnpm"
"3-4 h: fbzthx"
"2-8 w: wwnpwwxwwwcwzwwr"
"1-3 r: grrrr"
"12-13 d: pvddxddtsqgdd"
"4-18 w: vfsrcftqqllwqvqwhrgt"
"3-11 w: wnwqmfxfgkcxhmgh"
"17-18 l: lllllllllllllllllb"
"5-6 x: rvfxxx"
"10-11 n: nnnnnnnnnnnnn"
"1-9 s: wshhwwsscxps"
"2-12 k: bkvqsmzmjbckxvhtnkfb"
"7-10 l: ltlsnlrllm"
"1-5 n: nvnnn"
"2-4 m: gmpmz"
"13-19 k: kkkkwkkxkkkkpkfkkkq"
"6-15 l: dlhlcllllrllllll"
"14-15 q: qqqqfqcqqqqqqqsq"
"6-7 z: qzzdtzzqzz"
"1-4 v: pvvvkrgkvhmvvv"
"1-3 b: bfbcjdmb"
"6-9 b: gqbljxvmmbcbbkqgb"
"10-12 v: vvvvmvvhdrzv"
"2-3 t: tttt"
"9-13 p: jlhnpxnppwnpplqp"
"3-5 z: zdzcz"
"4-19 b: bbbbbbbbbrgbbdbbbbb"
"9-15 x: xxxxxxxxlxxxxxbx"
"1-5 f: sfffmf"
"8-12 w: lnlwfcwgtzhxlr"
"1-3 c: cclrc"
"8-12 p: jhkpfmltvpjpb"
"2-8 m: jmnmhkrmqvwx"
"7-9 p: pppppppndppp"
"7-9 k: kkkmkkkdkks"
"4-5 w: wwwwww"
"1-3 j: pjjj"
"3-4 z: xczz"
"5-6 h: nhdlvq"
"4-9 g: gggngrgtgggggg"
"6-9 l: klllltllrlll"
"1-3 k: mkkk"
"4-11 b: hfbbbfccxbc"
"4-10 w: wmhpzkswdwl"
"1-2 h: kphh"
"10-17 g: gggggggggggggggggggg"
"15-19 g: gggmggggggggggggggg"
"2-3 z: zqxl"
"8-10 p: pppphpppppppp"
"2-3 q: qhsqqqq"
"1-4 v: vqtvvlnpwvvnv"
"16-17 g: bgjpggsggggxggjgg"
"8-9 p: kpskgpklpkprqrtpjkdh"
"8-12 f: frxfhffpqqfw"
"3-4 d: dswjddd"
"5-9 t: ttwtttttdttttt"
"3-5 q: qqqqq"
"2-11 g: gggggggggggg"
"3-15 d: tddxdddddddsdvdx"
"2-3 d: dzmnd"
"4-8 j: gjjjjjjvkbjcbxp"
"5-18 l: djxdjmvntxwlnsftglr"
"3-6 b: bbhbbbbbh"
"17-20 k: kkzkkkkkrkkkkkkkhkkv"
"7-9 f: fvffffzfnff"
"4-10 t: tttkttttwwtt"
"3-5 t: vttmpzqxqtqnz"
"8-9 q: wkpkqsvvqmdq"
"3-6 q: qhqqqq"
"3-4 q: qdqqpph"
"2-6 t: vrzktf"
"2-3 n: nnnn"
"3-4 t: tbtw"
"5-12 v: zrwpjvpmxgncxknv"
"10-12 r: rrrrgdrrrzrs"
"3-4 k: qmmmbbnvvhvdwmfzk"
"5-6 j: jqzvjjjxj"
"7-13 v: vvvvvvvvvvvvkvv"
"7-8 p: kpppphppph"
"6-7 l: lzsfzlll"
"7-9 m: mmmmmmgmn"
"3-8 m: lmbxzdzrsq"
"14-17 k: ckhdnjzmvhtvbktskrk"
"5-10 d: ddpdpdjtnbdg"
"6-8 v: vtfzlwgdffhf"
"7-8 n: nkvnjsrnn"
"2-5 p: ppkppp"
"2-3 p: nppgpbr"
"1-3 k: dklkkkkkkkk"
"1-2 x: xxxx"
"2-4 d: dpdtddd"
"4-5 p: mlhpphxphv"
"14-15 x: xxdxdwkxxvbxwcxxx"
"10-11 f: jdfsmfxffffwfrfffhj"
"3-9 l: llbgcfzlnz"
"13-14 h: chhhhwhmqhhjhh"
"3-4 g: gmgkggg"
"6-7 q: qprdhdwsjnblqnkgf"
"9-10 r: rrrrwprhrr"
"2-5 g: jbjgl"
"7-8 x: xxxxxxnl"
"7-8 q: qqqqqqgr"
"3-4 v: vvvsv"
"3-4 w: wwhnjwwgw"
"1-8 f: mdqfrxfwfcf"
"2-4 v: gvhvwkvhfs"
"15-16 d: dcddddddddddddqnddd"
"13-14 v: kvkvvvzvshfkvpzvvvp"
"17-19 z: zzzzzzzzzzzzzzzzrzqz"
"6-8 k: kmkkkfgkkk"
"12-16 v: svxtcjxgdmkvqjfvzln"
"4-10 p: gljwppnhpc"
"8-15 c: ccccccccccccccccc"
"1-5 w: wwwwwwww"
"3-9 w: jwqgswwbtwwswwq"
"2-18 t: ptblkjvmjwglftpblr"
"8-11 n: hznznmrvjnm"
"5-6 q: qqqwrqq"
"4-10 s: scjssfsfcs"
"3-7 p: pppprpplpppzp"
"6-7 z: zzzzzpwzz"
"1-4 h: hhhh"
"14-16 r: rcrprqrxrrlrjrlrrrlr"
"4-6 x: xxxlxjxx"
"8-10 j: jjjjjjjqjcj"
"10-13 f: ffffffffftfff"
"8-9 r: rqrzrjhrr"
"7-11 m: tmfmhvmmpkmp"
"4-7 h: bjhhlhhh"
"2-3 l: lwll"
"10-11 s: jssssssssssssssssz"
"13-14 p: splrwgnphqclrmqf"
"9-11 j: jsjjjjltjjjjjzpjjdj"
"3-4 g: gpcwhg"
"5-7 s: ssbsssssss"
"5-8 w: bgwbjwwnwwwvww"
"9-11 f: fjcgtktnfpfxrqg"
"2-9 j: xgmdjfzsfhf"
"12-15 f: hkcgtffnzcffffffxdjb"
"5-10 k: kxggklgdrjz"
"6-8 b: bxbbbbbbb"
"4-10 m: tmqfmmmmmm"
"3-5 g: svtqgh"
"9-17 s: ssqssdrsstspssjssj"
"9-11 s: dssssssssslss"
"1-4 k: kckkqdkkmg"
"3-4 w: zbhwmkgqfqstwdwhs"
"1-2 j: jjjjnjj"
"10-14 w: rlwpdltwwtzdmnwgmdw"
"3-4 j: bjnx"
"14-18 n: nrnrnhnjnfwnnnnnrln"
"8-11 g: gvhwsbhghdgg"
"15-16 h: hghhhhhhhhhhhhht"
"2-12 x: xhxxxxxxxxxkxxx"
"8-13 n: xqnrnndtnznnkxb"
"3-6 t: rbnxbjw"
"6-7 v: vdfmjxvvv"
"1-13 x: xxxxxxxxxxxxxxxxxxx"
"3-9 m: mmmmmmmqmmmm"
"4-6 d: dddcdkddddcdgvzd"
"5-6 w: wwgwwhw"
"9-12 h: lmmwfqczxchc"
"12-15 x: xgpxxstxxxxxxxsrxz"
"6-10 c: wsnftlccckchtlqjhmt"
"8-9 f: ffffffzbd"
"7-10 z: zzzzbzhzzgzzzzzpzd"
"2-7 c: pccxccc"
"3-10 l: zlkmbdffdrhcwsc"
"5-6 x: xxxmxx"
"15-16 b: bbbbbbbbbbbbbbjtbbbf"
"4-6 m: lmmtnmrqwgmqmmmmw"
"7-15 j: jmpjrjjthvwjcljvnz"
"1-2 z: gqzj"
"1-6 h: hhhwhh"
"2-3 m: mzkm"
"7-9 z: zzhczvztz"
"6-7 w: vhkgmcwwjwgw"
"2-3 l: lsllllplllljlll"
"3-4 r: mvmr"
"10-12 h: hzbvhdfwthhhhjwhr"
"7-11 x: gstsnxjzhsmlnnwdcmt"
"12-13 g: pjmjghprgnxggf"
"3-4 m: rfmm"
"6-14 d: tsdlsjprjndfndhdmzhz"
"2-6 b: ppbbmhc"
"3-4 j: jjrkj"
"2-4 d: ddwd"
"2-3 h: mblfdbbkdjhhtm"
"4-5 q: qtqnd"
"2-6 g: ggggggg"
"3-4 c: cczdc"
"13-16 k: kvbgnklxkkwxkqlk"
"2-7 p: qphjpkpmzfpzlppw"
"5-8 c: ccccbccnc"
"2-10 k: kkkkkkkkkkk"
"15-16 x: xjxpxjxdkxlxfjqj"
"11-15 j: njjjsjjjjjcbjjt"
"1-3 z: mzzfz"
"1-5 f: fffffffffff"
"3-7 v: jvvwmjvjm"
"2-5 r: vrrkrrxfqrmv"
"15-16 v: sbvnlvvdvrbrwvvq"
"3-7 g: bwghkwggfm"
"7-9 v: vvvvvvvvjvv"
"3-7 m: gmmmmktmmb"
"6-12 t: mtbmttttkfth"
"5-9 c: ccpfchzpcdxcml"
"9-13 d: ddddddddbdddld"
"2-3 g: nrkg"
"4-8 m: mqnpqmxmq"
"2-4 p: pnpqpf"
"16-19 p: ppppppppppppppprppzp"
"3-6 j: jjjlmf"
"1-6 k: kbnpkkckwktwwqkcff"
"1-4 z: hzzg"
"5-7 b: bbbbbbbbbbbbbbsq"
"2-12 z: zwzzzzzzhzzzzzzzz"
"6-11 x: nddhcxbtgsxxcq"
"3-5 k: gkktkkh"
"2-8 f: wfnbhxlfstfwxrkhdxj"
"5-6 r: zcrrrr"
"1-2 p: dqjjwqjnqp"
"4-9 g: ggngjgggbggvg"
"3-6 m: mmsmcjmmmmmmmmmm"
"3-17 c: qvczjdtppwlvclclcw"
"8-9 k: kkkkkkkwdkkk"
"5-7 d: gddnldkddd"
"5-9 h: whkhvhrshllhldphhn"
"11-17 q: qqqqqzqqqqcqqqqqdqqq"
"5-6 k: fjszvkzmhshdd"
"6-8 k: kkkkkkzk"
"11-13 j: jjjjjjjjjjjjjjj"
"4-10 q: slwqqsqkbqqb"
"7-8 s: cvwvzswq"
"10-14 c: tvhxzvpdcckdzc"
"1-5 p: jpppppp"
"12-15 g: spggvdggsmfhggg"
"5-11 n: zlgnqkkqlhmrgn"
"11-18 j: zrjgljjljjjzjhjkrj"
"10-14 t: tttttttktdttttttcdtt"
"10-11 p: szxpqprpchkwvwqqk"
"9-14 t: ttttttgtmtfmttttttt"
"10-15 n: nnnnnnnznbpnnnxn"
"1-4 l: lllll"
"4-5 w: wbhhjpwbbft"
"10-12 r: rhrrlcrlrrmrrrwlrbx"
"13-14 g: ggggggggggggggggg"
"7-9 f: fvvwfffff"
"9-15 n: pnnnnnnnlndnnnnnnnn"
"5-7 b: bbbbbbbb"
"8-15 v: ldhwnvvwtxbskzvk"
"10-15 t: tgkkgtfttxtttqbtttv"
"5-15 s: hlsfskvqssskxds"
"2-7 g: wlnqrrdw"
"8-9 w: mwpbdlmmj"
"5-11 h: lclzlhhhhfvrrrzvnkfz"
"8-9 c: jcwdnxgnv"
"1-6 h: dchmhm"
"9-14 s: ssbdsvccsxtpnszv"
"3-5 d: dddddd"
"1-6 w: vwwwwf"
"5-6 f: lrffxb"
"16-17 n: nnnnnnnnnnnnwnnnnnnn"
"4-5 x: qlxjptn"
"4-5 d: ndddd"
"1-9 r: zrrrrrcrr"
"4-5 r: brnrr"
"15-16 r: rrrrrrrrrrrrrrhrrrrr"
"4-8 w: wwvdwwwwwww"
"12-14 f: ffffffdffffpfhfdg"
"3-9 h: srhvhkvsv"
"17-18 j: jzjjjjjsjjjjjjjjjj"
"4-8 t: lvpttpct"
"2-3 t: ttqt"
"3-11 v: wpvmlbvbpvs"
"10-11 x: vrkmmglwxxxsxsnxf"
"4-7 k: kkkkkkk"
"3-5 k: kkkkkkk"
"13-18 v: rkvvvlkzhvvmbgvvvk"
"1-2 p: prpppg"
"8-11 c: cxkchzcchccdzqfc"
"1-6 z: zzwzzz"
"3-4 z: czpdt"
"11-12 d: ddddddddddddc"
"6-8 l: llldlkvzll"
"5-15 n: wngptdmbvqftdvw"
"10-12 j: qjxmgghlbklxcpd"
"4-6 z: mdhzpzlw"
"11-13 c: cccccczgccccccccccc"
"5-10 z: zzzzxzzzzvzzzzmz"
"7-14 c: frhncvjxdcccbg"
"12-19 g: gggggggggggggggggggg"
"12-13 n: nwsknnnnnnnnnqtnnxn"
"11-12 d: ddpddddnrddw"
"8-9 s: bssssfsss"
"1-2 t: ttttttttttt"
"8-10 b: bbbbbbbrbfbbb"
"3-7 c: jwtdcccgj"
"4-5 j: djjjjhm"
"2-7 v: snsflvvrf"
"6-15 q: qqqqvrqqqqqqqqkqq"
"8-12 q: wbqqxvflbqxqzq"
"9-15 t: tttttztttjwdtsttpw"
"1-8 l: lllllllll"
"7-12 f: fffffffffffsf"
"4-5 m: lklqm"
"13-15 t: trtttttttthtgtt"
"4-5 q: qqqqqqqqq"
"1-10 r: prrrrrrrrhr"
"2-5 d: cprddmdhdvd"
"5-6 s: qsrxss"
"4-5 q: vwlvqqrplzqs"
"14-18 d: ddddddddlddddwdddgv"
"2-5 p: ppmqxptpp"
"12-13 w: wwwwwwwwkwwjtwww"
"6-7 f: spfffsnzc"
"9-16 s: zdmsgmcbspjtwsdspwvs"
"11-17 z: zzzzzzzzzzzzzzzzzz"
"11-16 j: jjjtjjcjjjbjbldv"
"6-12 b: bbbbbbbbjbbbbb"
"4-7 c: cccgcctc"
"3-4 f: fffjhf"
"10-19 g: ggjgggggjdggkgglggg"
"1-13 x: xvqpxzmjjxklx"
"6-8 k: kkkkkkkd"
"7-11 r: rhfrxrrttnrfrgqphr"
"10-11 w: hwwwwwncqwpwqwfvzww"
"3-4 h: hhmhh"
"1-5 n: zncnnwhcnqj"
"3-10 m: mmcmmmmlmcmmmmm"
"1-5 j: jjljx"
"5-8 b: bbbbbbbbbb"
"3-4 x: bvxxxxn"
"1-3 b: bfkbbbb"
"2-7 m: mjmmmmmm"
"4-7 n: znnnnnnn"
"12-14 h: kvlxhkdqbvwhhh"
"11-12 q: qlgqqqqdmqqqqqqsqn"
"2-5 p: pppppppvptvw"
"4-5 c: ccccccvr"
"1-5 b: xbqbn"
"7-8 p: pxnddnpgsp"
"2-3 j: nxxjs"
"1-4 j: vtdfk"
"7-12 l: mlcdlklmpbjl"
"4-6 l: lqgrml"
"12-14 v: vfplrnnvhlvhzk"
"2-5 x: xjkxbxxx"
"10-12 v: vvvvgvfjwvvjvvv"
"1-3 w: brprgblcpwhhp"
"3-8 n: nzdnnnnnnnvznnnnx"
"3-6 p: dghpfthx"
"8-9 r: frrrrrrmj"
"12-13 c: wnmxtcqqgcdcdpp"
"1-3 p: zpsp"
"11-12 z: zpzwzzszmgzgvztdzmrz"
"15-16 d: dxdqddddrdddddzzd"
"4-15 g: gbgrsgggjgggqdvnhggg"
"3-4 j: vjjmpl"
"17-18 b: bbbbbbbbbbbbbbbbbbb"
"14-17 h: vzhhhpqhqbgvghckh"
"6-16 w: wlwdwvwwbwwxwwwv"
"3-4 x: cxgj"
"10-12 t: ttjttztlgrtbttst"
"16-17 x: xtxxrxxxgxxxbqxfr"
"8-12 j: gjnnbxhgcgpd"
"3-4 b: pkkbfb"
"2-3 g: gggmgwgggggggghggg"
"8-10 z: zzzszzpjmzzzz"
"10-11 r: xbrkrjcsrtmrgtrrm"
"6-7 n: blmcznpnsbsw"
"3-4 n: nwzqznxn"
"6-9 j: jnjhvjxjjzc"
"4-5 d: qrddth"
"1-4 p: pphp"
"9-10 j: mhxwjjjbjj"
"5-6 l: llcllc"
"1-3 t: rtrttvtttttt"
"2-14 c: ccxccccfgcdccctbzgqc"
"3-7 k: kkrkkkq"
"5-10 z: zzzdqkzzgstqzzzz"
"1-3 w: pjbt"
"6-10 m: dlmsmrmmmmxmrmmmm"
"1-4 v: qvlsm"
"11-19 d: ddddddddddkdddddddpd"
"2-3 s: gsknvsrcwfbxnk"
"9-13 q: lvpvdqvzqndtbsrwjf"
"2-6 n: sjspfczdsnt"
"2-4 c: cccw"
"8-10 x: xqhcxzxxxxfdx"
"3-7 l: llltwlll"
"2-4 m: khqmnm"
"3-12 j: jvshgpptttfgkrnwf"
"11-12 k: kkkkkkpdkkkk"
"1-2 d: fcdd"
"11-12 l: dpnxdjhclqllqsd"
"8-9 p: tnphpwrppgm"
"6-7 c: frhvcll"
"4-9 x: xxxxxxxxxx"
"3-4 n: znnn"
"2-3 h: hmjw"
"7-8 m: qvtpmwmm"
"10-12 c: hbccgmvbhgccck"
"6-7 j: jjjjgjjjjjjjjjjj"
"3-6 m: rmrdgddjtmm"
"9-10 h: hhhhhhhhhhh"
"9-16 w: fwwwnmkwwjwcszwb"
"3-10 v: wkvxpxjcsvqgv"
"11-18 s: ssssssssssqssssssvs"
"5-14 v: bxbkvfvnvnvvwf"
"11-13 k: kdbkwbpkwjkkk"
"4-7 n: ncnnkvnnn"
"6-9 q: qxmvqmpqqdqsqjkhqq"
"6-8 p: ppppppspfpp"
"7-8 w: wwwhcsttd"
"18-20 t: tlrzstttttrttdmxhxtt"
"10-11 h: hhxzchbhhhshhbhv"
"14-17 h: jbfhhthndhwkhhbhh"
"12-13 t: tltttctbpmztrxnf"
"4-15 w: mbgcvdvhhwbpckxwsw"
"4-5 r: rrrrrlrvzrrhkr"
"1-3 q: qplqqdqqqqqvmqz"
"6-8 r: rvmrrftw"
"1-2 c: cczcrncddc"
"4-7 j: cjrbtlkxj"
"2-5 t: httgxlxfdskjgmdk"
"4-6 z: jtzzlv"
"8-9 d: ndndddddd"
"5-12 f: ncmjfbkmzxmfxfvnfnbw"
"2-5 z: zzfnz"
"1-6 d: sdddpr"
"12-14 v: vdvvvvvvvvvkvvv"
"11-15 m: jtgmzcmmmxnpvrtmmm"
"3-8 d: vqtddpdqdfddhcd"
"4-5 l: llplr"
"2-4 f: fcfzh"
"3-6 v: lbvklvp"
"15-16 k: kkkkkkkkkkkkkkkkk"
"6-7 c: ccccccccc"
"11-16 h: hhhhhhhhhhhhhhhsh"
"12-14 l: llllllwllllllllllll"
"11-12 v: bvslvwvzgwnv"
"4-5 l: xllllll"
"2-3 c: xccc"
"7-17 j: jjjjjjjjjjjjjjxjdjjj"
"18-19 w: wrwwwwwxwwplwhwwwww"
"4-5 z: tzzncf"
"1-2 g: gpgswkqsnxxkn"
"10-12 f: xpfffrxfqfcfff"
"14-16 r: rrrrrrrzxrrrrrrr"
"8-17 d: dddddddddddddddddd"
"7-11 j: kjvjgbjqkwjjjs"
"7-11 x: xxxxxxxxxxxxxx"
"13-16 d: cddddddgddddrddgdzd"
"11-15 x: xhpxxxxxxbktlxr"
"5-19 p: ppkpsnhkpttdqpvlhzp"
"10-14 f: xcfzqffcnfprzf"
"3-17 c: bdcmfmcptmhqczphc"
"1-12 d: ddddddddddmd"
"6-7 h: nnbphmjb"
"14-15 w: dmlvwvxwgcvfgwwl"
"7-8 v: qlvvvgjrcvwvvlszgvc"
"2-4 c: ncrc"
"5-7 q: qqmtqqqx"
"13-14 c: pcnbccwtcczcccg"
"1-5 t: dpgtlsw"
"12-13 f: zrcqtjjqjfrqp"
"6-12 n: mbhwrnnxzzjnlrmm"
"5-7 v: rvtrvhvtnvmvvmdv"
"9-14 g: ggggggggfggggl"
"1-13 q: gqqqgqqqqqqqpqq"
"8-15 k: tkdkdrgkdkktkrkdk"
"9-11 m: mpvmldmmbmj"
"2-6 c: chcccgclcrcc"
"5-7 l: llllhlllll"
"11-12 g: ggggggggggggg"
"2-3 x: bvcx"
"11-14 b: bbbbbbbbbqbsbb"
"3-6 x: xxxxxxx"
"9-16 g: bgggvwjhgmggpqjgv"
"6-9 n: ngsdrnnnknxgqdn"
"5-6 x: btjbxx"
"9-11 t: ttttctttdtktttt"
"6-7 s: ncxcsds"
"5-17 s: ssssssssssssssssss"
"3-8 t: ctdvrttftptt"
"9-10 j: fllmfjqjtqjjjtjgjjj"
"9-13 z: qzzhdznqfxrrrpw"
"4-6 k: hhkkqkwkk"
"12-13 q: qqdqqsqrrqqnx"
"4-6 j: hjtbnnfbhqbd"
"3-10 w: wwcqtplgdwzc"
"11-13 d: wdxddddcdvddddd"
"3-6 d: rcxlqm"
"7-8 w: wgcpwnxldswgc"
"6-10 p: pppppbpppwp"
"5-10 w: wbfwdgwfzrrlwft"
"10-11 c: ccccccccccbp"
"3-6 q: qqtqqbqq"
"12-15 k: kkkkkkkkkkkkkkk"
"12-15 x: xxxxxxxxxxxxxxxx"
"3-16 x: xvlxmxnnxxxkxxxj"
"3-13 z: zfzxglzkhzrbzpzdtn"
"6-14 f: mfffflfffffffzfff"
"10-12 m: lnnkhjthrndmcj"
"12-13 k: kkkkkkkkqkkjbk"
"3-4 c: kzcz"
"3-4 h: phhhl"
"5-15 n: nnnnnbnsnnnnnnqnnnn"
"12-16 v: zvccvkvcfvplvvcx"
"1-3 z: qzzzz"
"2-3 p: fjzkvmcsp"
"8-10 c: rccdvcckkcc"
"3-11 l: lllllllnlll"
"5-8 w: wwwdffwwwwgvwf"
"9-11 z: kjzrzzkhlzpzzzzzznl"
"9-16 t: ttttttttdttttttqttt"
"14-15 s: sfsfzlshbskndfcz"
"6-8 k: kkkkkkkkk"
"2-4 k: wpck"
"8-9 v: gtmcmvkvzbcrgvc"
"6-10 v: vvvvvmvvvvv"
"10-11 h: lhhhxhhhvwmmghfwk"
"8-11 w: wwwwwwwfwwlww"
"5-17 b: bbbbbbbbbbbbbbbbbb"
"4-11 j: jjjjjjjjjjjj"
"7-13 p: mpppppnnpppptcppp"
"10-11 w: wwwwwxwwmvwww"
"6-8 n: nmnsnknt"
"1-7 z: zzzzzhzzzb"
"2-6 v: kccntgvhvggvdfnq"
"16-17 g: gggggggggggggggxgg"
"6-8 v: brvpfvgvpvvgjpzq"
"2-10 w: sgnqldnccv"
"3-4 z: dzxkzzszzrpdgx"
"7-10 q: qqqtqqmqqqqq"
"4-9 x: xxxnxwxxjxxxx"
"10-12 d: ddddddddqddq"
"7-8 z: zrzzzzzs"
"1-19 w: wwwwwwwwwwwwwwwwwww"
"3-4 l: jqxlf"
"13-15 t: ctbllrttmtqttxt"
"12-13 p: ppbppppqfppts"
"6-11 p: pklpppljpcpgdpv"
"8-9 s: ssstsssss"
"13-16 t: ttttkvmttntwtpft"
"5-8 x: xkvxfxxpg"
"2-18 s: fgfrrxjqfrxskgkqvj"
"1-4 v: fwmlrv"
"9-10 x: xxxxxxxxxxx"
"6-13 f: wbwctctbsptfj"
"4-13 n: nnnnnnnnnnnnrn"
"8-9 n: nmnsnnmnnlhlhvjx"
"12-14 g: gggggggggggczv"
"5-8 r: rzqrrrrkzhr"
"12-17 k: kkkkkhkkkkxkkkkbkk"
"6-8 h: hhhhhhhqqmhh"
"1-3 h: dhmmghrhthhhvqpthf"
"3-4 t: ttkft"
"3-6 w: fwnwwgqq"
"8-9 h: whpwkhbhh"
"9-10 k: kkkkkkksbxk"
"4-6 k: qfkkrkwr"
"3-6 l: flllgl"
"6-7 z: zzzzzqmzzzzzz"
"2-3 h: zhhzh"
"4-9 t: gvqnsttftcd"
"3-6 c: zcbcsktcmhrkgc"
"5-8 m: zmqmmmmmmmmmmf"
"1-2 c: ccvcc"
"7-9 s: ssssssjstsssssssssss"
"12-19 t: ttftttttpnkttttttwt"
"5-6 m: lpqmmmfmvzb"
"9-11 d: ddddddddvdldd"
"7-9 k: kkkkkkkkk"
"12-15 l: lllllllllllpllllll"
"1-4 b: kzbbb"
"18-19 b: bxvlzxjgzbdbwfrjhvv"
"2-9 w: whwwwnwwcwwwwwww"
"4-11 f: ffffffffsff"
"5-6 v: fhvcvv"
"1-5 m: qqmpfmm"
"6-8 m: mmmmkvvhmcmmmmm"
"2-6 c: gcpvrcfhpsrpbtffnwk"
"5-6 q: sqkfqq"
"3-4 p: mbqppdqkdgkbf"
"8-11 b: bbbbbbbtbbpbbb"
"5-6 g: lmggqm"
"3-7 q: hnqhnqq"
"2-4 r: rrrlrd"
"7-8 r: rrrbrlrr"
"5-9 j: jjjdqjjjjjjjqjjckg"
"6-7 l: lllwpll"
"1-4 w: wxswwkw"
"17-18 w: wnxxmrvqmcgmntpfxnh"
"1-5 c: ccccc"
"4-8 v: vvxvvvvw"
"8-9 p: pppppppmpppp"
"1-7 z: zzzzzzmzzz"
"10-12 q: qqqqqqqqqssmqq"
"2-5 x: mxxnv"
"4-19 r: rrrlrrrrrrrzfrlrrrfr"
"4-8 k: kkkkkpxk"
"5-7 r: rfrqfbrrjv"
"3-6 h: hsvkkw"
"2-5 w: nwsfw"
"2-5 q: hqstqgq"
"6-15 n: mbmtgnvfzjnnjgnn"
"1-2 f: fffffff"
"1-7 v: vzvvvvvvxvvrrnzvv"
"3-9 h: whhhhhhhhhhnhhh"
"11-15 g: cgxhgsggnggrkgv"
"5-6 m: mmmmmmm"
"14-19 k: qkkkcvqjkklhkkkktkk"
"2-8 r: fcrrqrrgrrrrrrlr"
"1-2 l: lllvl"
"17-18 c: vmcbkchcdktrnxccht"
"10-14 l: klwzklwmllccql"
"4-7 g: xgfggwg"
"2-4 s: trhz"
"3-5 j: lzfglwfbsqj"
"4-5 p: stnprtpzszfc"
"9-13 p: pppnppppjtsppc"
"6-16 r: rxrrrrrrrdrbrrlrh"
"10-11 c: ccccvclccrl"
"8-9 l: nlglpwlqxl"
"10-11 x: xxxxxxxgsxx"
"7-8 z: zzzzszzlzwzzzzzzzz"
"1-5 q: qqnbc"
"2-3 v: jvvvv"
"2-6 f: btdfbcfnk"
"8-10 w: wlwnbwwblmww"
"3-13 v: brwmcxvlptbdvchwkjp"
"8-9 w: gwwwwwwbr"
"2-11 k: pkhzsvjbhkk"
"6-7 g: gggggmb"
"6-7 g: gggggggg"
"7-16 q: cqxfqzqnqvmkkhjqdr"
"1-13 r: rrrrrrrrlrrrrrr"
"10-14 x: xxxxxxxxxqxxxxxxxxxx"
"4-5 l: llllp"
"1-3 c: wccc"
"5-11 k: kkfgkkkkkkkkqhk"
"2-7 n: lnnjcks"
"12-14 s: sssssssssssssss"
"1-16 q: qqqqqqqqqqqqqqqzq"
"2-3 n: nnnn"
"8-20 m: vrtvfghfmskclmlmbwmm"
"2-4 n: nnwn"
"12-13 d: pdftgnmpcwddd"
"5-6 b: tsrbbb"
"4-7 q: zrppqcw"
"11-17 l: llllllllllllllllll"
"1-4 b: brzbfdgbphrzxtlpgj"
"7-8 x: xwlxxxxxxl"
"5-6 h: hhchnm"
"3-4 x: xxxxx"
"4-5 k: pkkqjkk"
"4-8 k: xqkkfwdkmsrr"
"7-8 l: lllllcsl"
"4-9 c: ccczcccccccccc"
"8-12 j: jjjjjjjqjjjjjjjj"
"9-11 j: vzkhqcjzkwjbpzv"
"11-12 r: rrrrrrrrrrtxr"
"1-4 t: mttbgtttttt"
"2-12 r: rrrrrrrzrrrrrr"
"10-11 c: ccccccccccgcc"
"9-16 d: bgdctdzjdxqfrbddznnp"
"3-7 s: brsjsdsh"
"3-11 j: cjwlbhgvcjc"
"13-16 j: pjfrdprjhmfqjddq"
"9-15 n: nnnnnnnnnnnnnnnnn"
"14-15 b: zbbbtbfbbbbbbbl"
"4-14 p: pppppppppppppjpp"
"3-6 j: pwbfjs"
"1-11 z: zzzzzzzzzzjz"
"7-17 d: gldddpskdbvmdmwgk"
"5-18 g: gggggggggggnmggggggg"
"6-7 g: llgggdh"
"4-5 j: zszjs"
"3-13 s: kwjbvbgxhwsbskjdkbv"
"1-2 c: kghcc"
"1-8 k: vtkthkhs"
"6-7 n: nnnnnnnnn"
"13-14 s: xssssssssssssq"
"3-4 h: hhxnh"
"8-10 g: gctrgrcgjg"
"7-9 n: nnncnnnnnn"
"7-8 b: bbnpbbbbb"
"6-11 x: jxqtcxxdxkxcwtxhdv"
"10-11 q: qqqkqkqqqqzqqq"
"5-6 k: kkkkkk"
"3-4 m: lndx"
"14-18 l: hdzlvpxlqnbklgpqgpz"
"14-18 f: ffffffffffxfffffff"
"4-9 p: gprzchppz"
"5-7 q: qqsljxk"
"7-8 q: pqqjqnkq"
"3-6 v: jvmvvvvvvjvf"
"2-10 l: hllsznczblmxbrmrnj"
"13-14 w: wwwwwwwwwwwwvc"
"4-8 m: mnmmmmmgm"
"10-11 r: rrrrrrwcrlq"
"3-4 q: qqqq"
"4-9 s: spwsjshpst"
"1-6 k: kkznkkkkk"
"2-6 t: dlbjpf"
"7-10 d: qxqbdtddgdvzmdmrp"
"16-18 b: bbbbbblbbbbbbbbvbs"
"1-5 c: cwbbccccccb"
"4-11 z: zrxzszzlzvzzzmdkt"
"17-19 b: bppptxztffxxqnlpbbb"
"3-9 n: nnnlncrnnnnn"
"""
INPUT_STRING_3 = """
........#..#.##.#..............
...#...............#.#.........
...#..#...#..##....#...........
...#.............#....#.....#..
..#......#..#...#.......#......
..............##...............
#.......#.........#......#....#
.#.....###.....#...#.#.#...#...
#.....................#....#.#.
.......#...................#...
...#.#...................#....#
....#....#.......#...#.........
..##.#............#..#.........
.....##.#..............##..###.
...........#....#....#.........
#.....#...#...#.#.#.#.##.#...#.
.#...............#....##.......
.....#..#......#....#.......##.
.....#........#.......#........
...#...##...#..##...#.....##...
.....#.........#.###...##...#..
.#.##...#........#.#.#.#....#..
....#......##.#...#.....#....#.
.......###..........#..#..#....
......#...#.##.................
....#...#...#.........#......#.
.....#...........#...###....#..
.....#...#.#.#....##.#......#.#
......#...#.....#..#..#........
#......#..#...##........###....
##.....#....##..#.#.###.#...#..
........#....#.......#.....#..#
#.#.#.##.#.#...................
..#...##....#......#.....##....
.......#.##..#........##..#....
.#.#....##......#.#..........#.
#..............#............#..
.#.#.#.#.#.####.#.#...##.......
.#..#.....##.#.......#.##...#..
..#.#........#.............#.#.
..#.#..........#..#........#...
..#..#...#.......##...#.#....##
...#.....#.#.#.....#....#....#.
.#...#......#.....#..##........
...#.......##.#.#.....#......#.
...........#.....#.#.......#...
#...........#...#..#.#........#
....#......#..##........#..###.
.#..#........................#.
#.......#......#...#...#..#....
....#.#...#..#.#....#....##.#..
.....#......#..#..........##.#.
.#.....#...........#.........#.
...###.#...#.......#.#.........
.......#....#..........#..#...#
......##..#.......#...##.......
..#..........#.......#.........
..........#..#..#..#..#........
.#.................####...#.#.#
..##.....#............#........
....#.....###...#......#....#.#
...##.#...........#.##......#..
#..##..#..#....#...#..#........
......#....#........#.......#..
......#.....#......###.........
.#.....#.#......#.......#......
..#.........#..#..#........##.#
..#.#....#.....#....##....#.#..
...#.............##............
........#..#..#......#...#.....
.....#.#...#...##.....#.....#..
.#..#.#..........##...##.....#.
......##.#..........#...#.....#
#.#.##......#....#..........#..
................#.......#.##...
#.......#.....#.......#....#...
#..#.....#.##..##...........#..
.....#....#.#.##..........#..##
#.......#.....#.##...........#.
........#.##........###..#.#...
........#..................#...
#.........................#...#
....#.........#...#.#..#.....#.
.#............#....#...........
..#.#...#..##...#.#.......#....
.#.#....#...........#.........#
...#.#..........#.....#...#....
......#....#.#...............##
....##......###...##.##.....##.
............#.#....#.#.....#..#
.....#..#.....#.#...###....#...
.......##....##..#...##..#...##
.....#.......##..#...#...#....#
#.........##....#........###.#.
...#..##...#...#.........#.#.#.
....#.#.....#.....#............
#........#....#..#........#....
.......#....#...#..............
#...#.........##.....###.#.....
.#....##..#...#..##.........#..
....#.....#......##..#..#....#.
#.#..#.........#........#......
..#.......#.........#.....###..
..#..........#...........#....#
..#...............#......#..#..
....#..#...#....###.....#..#..#
#...#...#..#...........#....#..
.#....#.#..#....#.#...........#
.....#.....#..#....#..#....#...
#.#..#...........#.#...........
..................#.#.......#..
...#.........#.....#..##....#..
.........#.#...#.........##....
...#..#....#.....#...#..#......
.#.##.....#....#....#......##..
##..#.........#.#....#...#.....
#......#.#...#....#.#..#.......
.......#.....#.....###....#.#..
.#....##.#.....#...#.......#...
.#.......#..#...#......#..#..##
...............#...#...........
#..............#....#.#.#....#.
...........#..#.......#.##..#..
..#......#.#....#...#.#.....#..
#..............................
#..#....#..........#...#.......
......#.............#####......
.#...###......#.#.#.##..#......
............#.##.....#.........
.........#....##....#..........
###....#......#.......#........
.#.......##..........#..#....#.
#..#.....................#....#
........#...........#..........
..#..........#...#..#.........#
..#..#......##................#
.....##..#...#..#..............
.......#...##..#...............
.......##..#.####....#....#.#..
#.#..#..........#........##....
....##....#.#..#....#.#...#....
......#.......#...#.....#...#..
..#..#...#.....#.......###.....
...#.......#.#.#.......#.##....
...............#..#.#........#.
.#....###.#......#.............
.#..#...#....#.#..#.....#......
.......#.##....#.#.##.##...#.#.
..#...#....#.#..##.#.....#...##
..#...#......#...#......#...#..
....#..#...#.#..#......#.......
#..#...............#......#.##.
.#....#...#..........#.#.....#.
.#..#.#.#................#..#..
.#....#.#...#..##.###..#...###.
#.............#.....#.........#
...#.........#...#.......#..#..
......#..#.........#..........#
........##................#..#.
......#...#.#.....#......##....
...............#...#....#......
...#.#..#..#.....##.###..##..#.
.#....##......#...#..##..#.....
.....#.........##.##....#...#..
.....#.#..................####.
#.....#...#.............##....#
#.#..........#...#..#..#.......
#..#.#.........#...............
....#...#.........#...##.......
...........#.....#..##..#......
#.....#.......#.#........#.....
..##..#.....#...##......#......
....#....#.....................
............#......#.........##
.....##.............#.....##..#
.......#.............#..#.#.##.
.###...#......#..#........##.#.
..#.#...#.#....#.....#..#......
..#.#..#.##........#...#.......
........#.#...............#..#.
........##.......#...#.......#.
...#........##.#..........#.#.#
..#..###.#.#.......#.#......#..
....#..........#...#..#........
...#..#...#...#.#....#...#..#..
...#...#........#......##...#.#
#...........#..........#..#.##.
...#..##..................#.#..
...##.#...#....#.#...#.####....
.....#...#.#.#..#..............
.....#..#.#.#..#...............
..#..#..##...#.#..#.....##....#
.......#.#..#.....#....#.......
...#..#....#.........#...#.....
..............#.#...#...##.....
...................#...........
.#......#.#...................#
.##.....#........#.........#..#
.##..##...#...................#
...#....#.#..#.#.#..#.....##...
.......#..#....#......####.#...
.##..#..##....#.......#........
.#...#...........##............
.....#.....#........#..........
....##..#....#.....#...........
.#...#....................#....
....#.........#.......##.....#.
.#....#..#.....#.##....#.......
....#..#.........#.#....#.#....
.......#.........##....#.......
..#......#....#....#...#.......
........#..#.......#.##......#.
..#.....#......#...#..#.......#
#..#.....##...#...#............
.......##.......#........#...#.
..#......................#...#.
....##.#.............#......#..
#.#............................
...##.#.....#.#............#.##
......#...#..#.........##......
.#.......#.....##.......#.#....
...........#.#.........#..##...
...#..........#.##....#........
........#..#..#...#....#....#..
........##....#.#....#........#
..#........##....###....#......
#................###...#...#...
................#.#..###......#
..#.....##.#................#..
.....#...............#..#......
..#.......####.....#..#.#....##
..#.....#..#....#..............
#.#...........#.#.....#..##....
#.#..........#.......#...#.###.
........#....#...#..#.#........
.#.....#......#..#..#..###..#..
.#.........#.##.#.#......##....
..#.........#...##..#........#.
.#...................#.........
...#.#........#................
............#.....#..##........
..#.....#.#......#.......#...#.
........#....##..##...#.....##.
.#........#.#....#.#....#.#..#.
#.#.......#....................
.#..#...##.........#..#........
.........#...............#.....
...#...#.....#......#.......#..
###......................#.#..#
...#.....####........#..#.....#
#.#...#.#...................##.
.........#.....................
#..........##..#.....#....#....
.......#...#.#.##.#..##........
..........#..#.#..#.#.......#.#
.....................#.#...#...
...........#.#........#.#.#....
.......#......#........#...#.#.
.........#....................#
.##.##....#...#.#.#.#..........
#....##..#.##....#....#.......#
.##.#...#...............#....#.
.......#...#.###....#..........
.....#....#...#..#.............
#.........#.##....#.#.#........
..#...#.............##..#..#...
#..##.......#..........#...#.#.
.#..#.....#...........#......#.
......#......#..............##.
.#...#..#...#..####.....#.....#
....##.......#..........##.....
.#.....#.......#.....#.#...#...
..#..#..#.#...#......#.........
......#.#....#........#.......#
........#.......#..............
..#...#.#....#........#.......#
............#....#...##.#......
.........#.............#..#....
#.............#.#..##.......#..
#....#...........###....#......
...#.....................#.....
....#.#..........#...#.......#.
......#..#.......#...#...#....#
.#.#..#.....##.#........#......
...........#...#.#.............
...###............#...#..#.....
..#.#.......#...#.#..#.........
.#......##...........#.....#.##
.....##.....#....##...##.#.#...
..........#.#.#......#........#
..#.#........#....##....#.#....
.#....#...##...........#....#..
##......#...#.......#..........
.##...###..#...#......#..##.#.#
...........##.#..##...#.......#
..#..............##............
........#..#........#...#..#.#.
..#.............#......#...##..
#...##....#...#....#....#.#....
.#.#......#..##............#.#.
.....###.#....##....#....#.....
#.#.#..........#...#...#.#.#...
.....#.#...........####........
.....#....##...#.##..#......#..
#....#.......#.##.......#..#...
.....#.....#........#..........
.......#.......#...#.##......#.
...#.........##...#.#.#......##
#........#........#...#..#.....
.#......#.#......#.#...#....#..
#..#....##.....##..............
...#.##............#..........#
.....#.#....#..#.#............#
..#......#...###.##.......###..
........#....#.#.#.#...........
............#..#........#.....#
....#...............#..........
......#....#....###..#.......##
#...#...##....#.........#...#..
...........#.#.............#...
...#..#.....#..##.#....#......#
..#...#..#...#......#..........
....#..#....#.......#........#.
"""
INPUT_STRING_4 = """
eyr:2024 pid:662406624 hcl:#cfa07d byr:1947 iyr:2015 ecl:amb hgt:150cm

iyr:2013 byr:1997 hgt:182cm hcl:#ceb3a1
eyr:2027
ecl:gry cid:102 pid:018128535

hgt:61in iyr:2014 pid:916315544 hcl:#733820 ecl:oth

hcl:#a97842
eyr:2026 byr:1980 ecl:grn pid:726519569 hgt:184cm cid:132 iyr:2011

ecl:grn hcl:#6b5442 pid:619743219 cid:69 hgt:176cm eyr:2027 iyr:2012
byr:1980

ecl:brn byr:1969 iyr:2014
hgt:164cm eyr:2020 pid:982796633 hcl:#602927

ecl:gmt
iyr:1987 eyr:2039 pid:15115163 byr:2006
hcl:bfab0d

cid:117
hcl:#efcc98
iyr:2010 pid:322719183
hgt:176cm
eyr:2020
byr:1957
ecl:brn

byr:1954 hgt:178cm hcl:#38f7fd pid:838813262 ecl:blu
eyr:2029 iyr:2019

eyr:2023 ecl:amb iyr:2020 byr:1927 pid:242570886 hcl:#18171d hgt:192cm

iyr:1990 cid:295 hgt:131 pid:187cm byr:2014
ecl:xry hcl:z
eyr:1928

ecl:hzl
byr:1953
eyr:2023 hcl:#866857
hgt:181cm iyr:2010 pid:568185567

byr:2030 hcl:#fffffd ecl:#a4a596 hgt:168cm
iyr:1936 eyr:2020 cid:296 pid:168786676

byr:2030 iyr:2026 eyr:1974 hcl:7fcaa5 ecl:utc
pid:190cm
hgt:67cm

byr:2023 eyr:2037 hgt:59cm
ecl:lzr hcl:z iyr:2026 pid:#ea9083

byr:2003 hcl:z hgt:91 iyr:1990 eyr:2024 ecl:#123d73
pid:48494230

byr:2022 eyr:2020 iyr:2030 ecl:gmt
hgt:191cm pid:3509331253 hcl:#888785

iyr:1994
ecl:#c3d564 byr:2009
hgt:162cm hcl:336498 pid:#e99d09
cid:288
eyr:1921

byr:1924 cid:290 iyr:2010 ecl:amb eyr:2020
hgt:156cm hcl:#7d3b0c pid:795497164

cid:301 iyr:2017 hgt:67cm
hcl:#888785 ecl:#0405b9 byr:1964 pid:707857518 eyr:1976

ecl:gry pid:474303066
iyr:2011 hcl:#18171d hgt:165cm byr:1921 eyr:2024

hcl:#6b5442 ecl:amb iyr:2020 hgt:191cm
byr:1949 cid:301
pid:075846582 eyr:2029

hcl:#a97842 cid:186 iyr:2014
ecl:gry
hgt:191cm eyr:2023 pid:645548969
byr:1956

pid:154cm hcl:z ecl:gmt iyr:1989 hgt:69in cid:53 byr:2010

hgt:72cm byr:2023
eyr:2034 hcl:z ecl:#f5249e iyr:1997 pid:#79af7a

eyr:2038 byr:2015
hgt:70cm ecl:grt hcl:9d58a1 iyr:1926 pid:6290928420

pid:620857794 eyr:2022
byr:1950
hgt:159cm
hcl:#ceb3a1 ecl:amb iyr:2015

eyr:1954 ecl:#ab2ce4 pid:#14eedd
iyr:2009
hcl:29e484
byr:2022 hgt:73cm

hgt:59cm byr:2026 cid:245 iyr:2020
eyr:2029 pid:073943129 ecl:hzl
hcl:#b6652a

iyr:2014 byr:2015 hcl:#a97842 eyr:2029
pid:#132098
hgt:150 ecl:oth

hgt:151in ecl:#967d49 eyr:2026 hcl:#18171d
pid:384230726 byr:1934
iyr:2018

iyr:2020 eyr:2021 byr:1937 pid:735047371 cid:159 ecl:blu hgt:177cm hcl:#22b774

ecl:brn hcl:#6b5442 pid:117807698 cid:105 iyr:2016 byr:1977 hgt:183cm

ecl:hzl hcl:#6b5442 byr:1933
iyr:2019 pid:348486702
eyr:2020 hgt:193cm

byr:1928
ecl:gry
eyr:2028 hcl:#fffffd pid:571149069
iyr:2012 hgt:175cm

pid:359108298
eyr:2027 hgt:158cm ecl:amb iyr:2016
hcl:#602927

iyr:2027 byr:2015
hgt:191in pid:102033301 ecl:xry
eyr:2031 hcl:#602927

ecl:oth cid:163 hcl:z iyr:2014
byr:1944 hgt:173cm
eyr:2027 pid:#0524c1

ecl:brn
byr:2030 hgt:71cm eyr:1931 cid:165 iyr:2010 hcl:#cfa07d
pid:509642098

hgt:166 iyr:2020 cid:308
eyr:2022 pid:950463527
byr:2017
hcl:z

ecl:amb
eyr:2023 byr:1924
pid:901038027 hgt:70in
iyr:2010 hcl:z

byr:1972
iyr:2013
hcl:d669ad hgt:64cm cid:247 ecl:#19aa26 eyr:2023

hgt:71 hcl:#fffffd
byr:1976 cid:108 eyr:2038
ecl:grt iyr:2018 pid:190cm

iyr:2017
byr:1963 ecl:grn hgt:175cm
pid:160915270 eyr:2028 hcl:#cfa07d

pid:569740130 hgt:171cm hcl:#733820
ecl:gry eyr:2024 iyr:2020 byr:1973

byr:1937
iyr:2016 ecl:gry hgt:181cm pid:521705827 hcl:#b6652a eyr:2027 cid:295

hgt:156cm ecl:blu iyr:2019 hcl:#866857
pid:662418718 byr:2000 eyr:2024

byr:1971 pid:693616099
hcl:#efcc98
hgt:175cm iyr:2016 ecl:gry
eyr:2023

iyr:2013
eyr:2024
ecl:gry
pid:414295491 byr:1986
hgt:188cm hcl:#b6652a

eyr:2022 byr:1975 iyr:2020
ecl:grn cid:68 hcl:#a97842
hgt:151cm pid:229803943

cid:258 iyr:2012
ecl:hzl
byr:2001
eyr:2021
hcl:#866857 pid:990590217 hgt:172cm

cid:339 byr:1957 hcl:#866857 pid:343480061 eyr:2039
hgt:191cm
iyr:2021
ecl:utc

cid:281 hcl:z ecl:blu
byr:2020 pid:132694306 eyr:2020 iyr:1953

hcl:#602927
byr:1933 eyr:2028
hgt:165cm ecl:gry iyr:2018 pid:658484617

ecl:oth
hgt:188cm cid:110 pid:056975690 iyr:2016 byr:1950 eyr:2023 hcl:#cfa07d

cid:342 hcl:#fffffd eyr:2024
pid:153555359 byr:1974
ecl:gry hgt:191cm iyr:2020

byr:2019 ecl:#160ed3 eyr:1999 hcl:z
cid:146 pid:195693972 hgt:159cm

iyr:2015 eyr:2030 hgt:191cm byr:1979
ecl:#ec4873 pid:994113786 hcl:#cfa07d

pid:552331609
ecl:grn
hgt:171cm eyr:2022 hcl:#b6652a
iyr:2020 byr:1931

hgt:177cm iyr:2010 pid:934058099
eyr:2020
ecl:blu
byr:1967
cid:112 hcl:#7d3b0c

iyr:2028
hgt:138
cid:180 hcl:z
eyr:2022 pid:3286566621 byr:2002

eyr:2020
iyr:2019
hcl:#a97842 pid:149148750 ecl:brn hgt:159cm
byr:1981 cid:339

cid:344
eyr:2021 byr:1968 pid:777786047
ecl:grn hgt:192cm hcl:#888785
iyr:2015

hgt:173cm
eyr:2030
hcl:#733820 pid:610226642 byr:1954 cid:80
iyr:2013 ecl:blu

byr:1999 eyr:2023
ecl:amb pid:912145128
hgt:181cm
iyr:2015 hcl:#a97842

eyr:2027 hgt:188cm
pid:080715145 hcl:#341e13 iyr:2013
ecl:oth
byr:1965

hgt:170cm byr:1950 iyr:2013
pid:010541784
eyr:2027 ecl:zzz
hcl:a3bae8

hgt:190cm eyr:2024 ecl:#6dcedc pid:909319684
iyr:2011 byr:1959 hcl:z cid:182

eyr:2028
iyr:2016 hcl:#623a2f pid:208417572 byr:1929 cid:137 ecl:hzl
hgt:167cm

hcl:#6b5442
ecl:grn
byr:1938
eyr:2023 cid:307
hgt:59in iyr:2014 pid:205268145

pid:047489285 eyr:2026
hcl:#b6652a byr:1920
iyr:2015
hgt:183cm ecl:gry

ecl:blu hcl:#508e8b iyr:2016 eyr:1954 hgt:151cm pid:086752750 byr:1920

iyr:2011 byr:1981 hgt:186cm
cid:117 hcl:#6b5442 ecl:amb
pid:756830713 eyr:2026

eyr:2037 pid:364464758 hcl:z ecl:grn
hgt:112 iyr:2013 byr:2022

ecl:hzl
cid:65 pid:679487194
byr:1986 hgt:169cm hcl:#cfa07d eyr:2025 iyr:2013

cid:192
byr:1921 pid:#5fe831 ecl:#fbb2b9 hgt:62cm eyr:1971 iyr:2024
hcl:z

hcl:#cfa07d eyr:2026
hgt:74in
iyr:2019
ecl:xry
pid:622690982 byr:1982

eyr:2026 pid:523515724 iyr:2013 byr:1973 hgt:167cm
ecl:grn hcl:#866857

byr:2009
eyr:1985 pid:484497014 ecl:#0bfcf2 iyr:1992 cid:131 hcl:39d6b0 hgt:177in

eyr:2020 iyr:2016 ecl:brn hcl:#ceb3a1 byr:1966 pid:696621560 cid:62
hgt:59in

hgt:166cm hcl:#7d3b0c
iyr:2016
ecl:brn pid:190cm
eyr:2020
byr:2001

eyr:2021
iyr:2012 hcl:#6b5442
ecl:amb hgt:169cm
pid:969150085
byr:1925

ecl:brn hgt:175cm byr:1992 iyr:2016 pid:415209726 eyr:2027
cid:72 hcl:#866857

iyr:2017
hcl:#733820 byr:1938 eyr:2020 pid:274486958 hgt:163cm

hcl:4f5dd1 cid:336 ecl:grn iyr:1931 pid:6212280197
byr:2016 eyr:2037
hgt:187in

iyr:2017 byr:1940 eyr:2025 pid:115098205 hgt:151cm
ecl:grn
cid:122
hcl:#6b5442

hcl:#efcc98
iyr:2020 pid:709548547 hgt:179cm
eyr:2030 ecl:gry byr:1975

cid:217 hcl:#888785 eyr:2029
ecl:hzl iyr:2013 pid:160053490
hgt:166cm byr:1992

eyr:2024 cid:188 iyr:2016 hcl:ff3a59 ecl:xry pid:296357512 byr:2026

hgt:154cm iyr:2010
ecl:blu pid:717041634 byr:1928 cid:123
eyr:2027
hcl:#a97842

pid:391011205 ecl:hzl hgt:191cm iyr:2016 eyr:2028 cid:281 byr:1934

byr:1937 hgt:65in
pid:667975382 ecl:gry cid:270 eyr:2024
iyr:2012

hgt:179cm pid:065528723
hcl:#888785 byr:1937 eyr:2028
iyr:2013 ecl:hzl

iyr:2027 cid:261 eyr:2037 ecl:#ced7d5 pid:157cm
hcl:3a80c1 byr:2029 hgt:187in

eyr:2028
hgt:157cm hcl:#733820
iyr:2012 ecl:blu byr:1952 pid:915063263 cid:335

eyr:2023 hcl:#efcc98 pid:490625944 byr:1961 ecl:grn hgt:155cm iyr:2018

cid:247 pid:2807544665 eyr:2021
ecl:oth
hgt:191cm
byr:1928
iyr:2013 hcl:#623a2f

eyr:2015
byr:2021
hcl:40d2fc hgt:69cm pid:159cm ecl:gmt

hgt:175cm eyr:1992 cid:328 pid:263110997 ecl:#e53989 byr:2014 hcl:#a97842 iyr:2026

pid:491396731 eyr:2027 hgt:172cm hcl:#623a2f cid:92 iyr:2017 byr:1983 ecl:grn

hcl:#fffffd
iyr:2018 byr:1983 pid:714591144 ecl:grn eyr:2021
hgt:160cm

eyr:2027
hgt:63in ecl:blu byr:1987 pid:397963077 iyr:2018 hcl:#ceb3a1

eyr:2027
hgt:184cm
hcl:#6b5442 iyr:2012 byr:1984 ecl:blu pid:196287205

iyr:1998
ecl:hzl
pid:7872103596 byr:1991
cid:275 eyr:2039
hgt:174cm hcl:0d2ad6

iyr:2010 hcl:#efcc98
byr:1992 hgt:65cm eyr:2038 pid:383236012 cid:68 ecl:lzr

hgt:190in cid:127
byr:1947 pid:515728209 hcl:#733820 iyr:2014 ecl:amb eyr:2020

iyr:2017 eyr:2028
hcl:#623a2f
byr:1964 ecl:grn pid:198467794 hgt:169cm

ecl:utc
hgt:59cm byr:2007 iyr:2030
hcl:7ac4db eyr:2038 pid:#7206c6

iyr:2010
hcl:z eyr:2021 ecl:brn
hgt:173 cid:86
pid:194240791 byr:1975

pid:9347286034
hgt:63cm
iyr:1992 eyr:2034 hcl:66031b ecl:grt byr:1929

pid:593398904 byr:1939 iyr:2019 hcl:#b6652a ecl:gry eyr:2023
hgt:70cm

byr:1991
iyr:2019 hgt:164cm pid:282852411 cid:340 ecl:amb
hcl:#341e13 eyr:2027

eyr:2020
iyr:2014 ecl:grn hcl:#866857 hgt:158cm
byr:1931 pid:321748597

cid:98 byr:2023 iyr:2019 pid:#48f79f
hcl:73c882 eyr:1973 hgt:151in
ecl:utc

iyr:2023
hcl:#18171d
pid:52221892 eyr:2039
byr:2008 hgt:72cm ecl:#db8d14

iyr:1966 cid:274
eyr:2034 pid:12256322
byr:2006 ecl:dne
hcl:985c2d

hcl:#fd033b
eyr:2026 ecl:blu
iyr:2016
byr:1953 hgt:157cm
pid:502619036

byr:2015 pid:159cm iyr:2025
hgt:158cm eyr:1943 hcl:z ecl:grn

ecl:blu iyr:2016
pid:842400950
hcl:#733820
cid:266
eyr:2027 byr:1931
hgt:161cm

iyr:2017 hgt:190cm byr:1994 pid:706570967
ecl:hzl hcl:#18171d
cid:180

cid:197 pid:204952666 ecl:amb
hgt:70in iyr:2016 byr:1936 hcl:#98cbe3 eyr:2025

pid:555499128
byr:1971 hgt:71in
cid:83 ecl:blu
hcl:#cfa07d eyr:2027

ecl:hzl iyr:2014
pid:30428184 cid:237
hgt:171cm byr:1942 hcl:#888785 eyr:1986

eyr:2025
pid:579385370 hgt:193cm
hcl:#c0946f byr:1979 iyr:2016
ecl:amb cid:284

eyr:2029 byr:1946 pid:278271295
ecl:grn
hcl:#cfa07d cid:271
hgt:172cm
iyr:2020

pid:731752614 eyr:2020 byr:1983
cid:248 ecl:oth hgt:179cm
iyr:2017 hcl:#fffffd

hcl:z
cid:203 eyr:2032 ecl:#3f9d3d hgt:65cm pid:4042846885 byr:2019
iyr:1946

hgt:171cm ecl:gry eyr:2027
iyr:2013
hcl:#7d3b0c pid:92288579
byr:1955

ecl:brn hgt:164cm byr:1969 hcl:#cbf9c9 pid:022724981 eyr:2030 iyr:2013 cid:244

hgt:162cm byr:1974 iyr:2015 pid:927525094 hcl:#3d3011 ecl:blu
eyr:2023

hgt:157cm
eyr:2020
pid:221286943 hcl:#fffffd ecl:amb iyr:2018 byr:1945

iyr:2019
eyr:2025 byr:1997 pid:341544323 hgt:174cm cid:113
ecl:hzl

pid:138492032 hcl:e35302 ecl:#caaede
eyr:1931
byr:2001 hgt:156 iyr:1998

pid:912182030 cid:189 hgt:162 hcl:#277b39
iyr:2013 eyr:2023 byr:2023 ecl:blu

eyr:2027 hcl:#fffffd
ecl:brn
cid:304 iyr:2016 byr:1969
pid:866607511 hgt:192cm

hgt:64in
ecl:amb
byr:1958
pid:720439412
iyr:2015 eyr:2022 hcl:#ceb3a1

eyr:2024 hgt:159cm
pid:187867283 iyr:2016
ecl:oth hcl:#fffffd
byr:1988

ecl:#910bf2 byr:1969 iyr:2011 hcl:z eyr:2024 pid:579502502
cid:103 hgt:174cm

pid:718692455
eyr:2028
iyr:2016
hcl:#602927
ecl:blu byr:1954
cid:251 hgt:182cm

eyr:2021 hcl:#341e13 ecl:amb
byr:1933 hgt:179cm iyr:2011 pid:083172316

iyr:1998 hcl:z eyr:1944
byr:2006 pid:453368738
hgt:160 ecl:#9da5f1 cid:261

hcl:#7d3b0c
iyr:2018
hgt:164cm eyr:2020 byr:1940 ecl:blu

pid:993701676 eyr:2028 ecl:gry
byr:1951 hcl:#888785 cid:116
iyr:2020
hgt:192cm

hcl:z eyr:2033
ecl:lzr iyr:2029 cid:326 hgt:68cm byr:2026
pid:96742419

hcl:#a97842 ecl:brn
byr:1920
hgt:173cm iyr:2015
eyr:2024 pid:176967666

byr:1930 eyr:2025 pid:792694131
hgt:179cm ecl:brn
hcl:#a97842
iyr:2015

hgt:167cm byr:1960 eyr:2022 hcl:#efcc98
cid:87 ecl:blu iyr:2012
pid:431515059

hcl:#cfa07d
eyr:2023
hgt:188cm ecl:grn pid:081575957 byr:1938 iyr:2012

iyr:2010 byr:1973
cid:108
eyr:2026
pid:880191154 hcl:#888785 hgt:181cm
ecl:brn

eyr:2021 iyr:2010 byr:1942 hcl:#7d3b0c ecl:hzl pid:886241926 hgt:171cm

cid:53 byr:1993
pid:150cm eyr:2035
hcl:#888785 hgt:153cm ecl:#128262 iyr:2021

ecl:gry
pid:555911148
hcl:#733820 eyr:2022 hgt:154cm iyr:2012
byr:1935 cid:338

hcl:#b6652a
pid:833873846 iyr:2012
hgt:167cm eyr:2023 byr:1984

eyr:2024
ecl:blu byr:1955
hcl:#b6652a pid:517975316 iyr:2010 hgt:166cm

pid:133785752
ecl:blu
eyr:2024
byr:1973
iyr:2019 hcl:#fffffd
cid:236 hgt:173cm

cid:222
byr:2013 hcl:z eyr:2036 pid:7443967478 ecl:brn
iyr:2030 hgt:62cm

hgt:193cm cid:259
hcl:#18171d
ecl:grn
byr:1995 pid:727880050 eyr:2030 iyr:2010

hcl:#c0946f cid:275 eyr:1954 pid:772184635 ecl:#76add7 byr:2009 iyr:2018 hgt:151cm

ecl:#52ed0f eyr:2033 hcl:#18171d pid:475397948
byr:1946 iyr:2028 hgt:178cm

iyr:2012 hgt:152cm
eyr:2027 byr:1923 ecl:brn
hcl:#18171d pid:513722888 cid:171

iyr:2029
hgt:111 hcl:z ecl:#33e3bc eyr:1930
byr:1934 pid:94036732

hgt:154cm eyr:2024 hcl:#6b5442 iyr:2017
byr:1974
ecl:amb pid:470968353 cid:345

hgt:184cm hcl:#617375 eyr:2028
byr:1975 ecl:oth
iyr:2018 pid:735589126

cid:261
hcl:#cfa07d pid:213013397
hgt:187cm
ecl:gry iyr:2016

hcl:#623a2f
ecl:#34964b eyr:2009 pid:169cm byr:2028 hgt:169cm
iyr:2028

eyr:2029 iyr:2016
byr:1985
hgt:192cm hcl:#602927 cid:167
ecl:blu pid:620818510

eyr:2029
byr:1968
ecl:blu
hgt:183cm iyr:2011 pid:952376140 hcl:#efcc98

iyr:2020
byr:1981 pid:850136149 eyr:2028 hgt:159cm hcl:#7d3b0c
ecl:brn

ecl:brn pid:480452858 hgt:65in cid:340 eyr:2022
byr:1946
hcl:#602927 iyr:2015

hgt:172 hcl:z eyr:1958 iyr:1941 byr:2019 pid:389995951 ecl:dne

byr:2025 hcl:4c8dcd
hgt:177in
ecl:#55d635
cid:197 pid:91192572
iyr:1921 eyr:2038

iyr:2027 pid:154cm
hgt:185in byr:2012
eyr:2036 hcl:efd47d
ecl:#64f98d
cid:86

eyr:2029 pid:837224515 ecl:grn cid:231 hcl:#733820 iyr:2019
hgt:159cm
byr:1977

pid:974518338 byr:1964 hcl:#cfa07d ecl:grn eyr:2030
hgt:61in
iyr:2019

iyr:2019
hgt:192in cid:94
eyr:1922
byr:1925 hcl:z ecl:utc pid:#081266

eyr:2027 iyr:2019 cid:328 byr:1961 hcl:#6b5442 ecl:blu hgt:177cm pid:235426720

byr:1959
eyr:2025
pid:890034625 ecl:oth
hgt:62in cid:348 hcl:#733820

hgt:161cm iyr:2018 pid:916160791 ecl:grn
byr:1951 hcl:#44d03a eyr:2025

hgt:158cm byr:1942 iyr:2012 hcl:#602927
eyr:2026 ecl:gry pid:651231060

ecl:hzl cid:340 pid:086942161 byr:1986 hcl:#a97842 iyr:2018
eyr:2028
hgt:181cm

ecl:blu
pid:278922687 cid:238 iyr:2018 hgt:153cm eyr:2027
byr:1965
hcl:#733820

eyr:2023 cid:208 hgt:178cm hcl:#341e13 byr:1937 pid:290981079 iyr:2010 ecl:grn

hcl:#888785
ecl:amb
byr:1943 pid:559804716 eyr:2026 hgt:166cm
iyr:2019

pid:947831563
ecl:gry
byr:1960 hcl:#341e13
iyr:2016 hgt:173cm eyr:2029

ecl:blu iyr:2016 pid:724632073 hcl:#623a2f
eyr:2028 hgt:192cm byr:1958

byr:2021
eyr:2016 hcl:z iyr:1988 pid:65353943
ecl:#bb553b
hgt:125

hcl:#efcc98 byr:1963 pid:290433211 eyr:2023 ecl:hzl
hgt:172cm iyr:2013

iyr:2015 ecl:brn
byr:2023 hcl:#18171d
pid:325330679
hgt:190in eyr:2023

pid:745674970 hgt:160cm eyr:2021 byr:1925 ecl:gry hcl:#341e13 iyr:2015
cid:297

eyr:2021
pid:596411633
byr:1947 ecl:blu cid:191 hcl:#341e13 hgt:168cm iyr:2019

eyr:2030 pid:#902a6b iyr:1997 hcl:11f396 hgt:188cm byr:2025
ecl:dne

eyr:2025
byr:2006
hcl:#888785 ecl:hzl hgt:187cm
iyr:2012 pid:017702828

byr:1988 hcl:#18171d iyr:2019
pid:110591871
ecl:hzl
hgt:160cm
eyr:2029

ecl:brn
hcl:#c0946f iyr:2030 pid:264404022 byr:1984 hgt:59cm eyr:2040

pid:5973803069
hcl:#cfa07d ecl:grt
hgt:153cm eyr:2039 byr:1970
iyr:2025

hcl:#fffffd
iyr:2022 byr:2026
hgt:180 pid:82035145 eyr:2034 cid:118 ecl:utc

hgt:186cm eyr:2026
ecl:brn
iyr:2013 hcl:#8f4c9b pid:010260339 byr:1948

ecl:amb hcl:#18171d iyr:2020 pid:259501214 byr:1978 hgt:193cm
cid:263 eyr:2022

hgt:161cm iyr:2015 byr:2014 eyr:2003
pid:708958872 ecl:grt
hcl:f4a430

hgt:170cm eyr:2021 pid:911638274 cid:110 byr:1963 ecl:blu
iyr:2015 hcl:1eda64

ecl:oth byr:1949 hgt:174cm hcl:#18171d eyr:2022 iyr:2019
pid:305857230

ecl:gry hcl:#a97842 pid:971971076 byr:2002 iyr:2019
hgt:188cm
eyr:2022 cid:238

eyr:2027 pid:221315043 iyr:2010 hgt:159cm ecl:blu byr:1998 hcl:#6b5442

hcl:#888785
byr:1926 eyr:2022 pid:433807814 ecl:grn
iyr:2010
hgt:181cm

ecl:grn hgt:164cm byr:1951 hcl:#18171d cid:75 pid:845508281 eyr:2021 iyr:2017

pid:#f59bc7
eyr:1987 hgt:191cm hcl:z byr:2024
iyr:1985

hcl:#623a2f pid:497429747
hgt:189cm
byr:1987
eyr:2027 iyr:2012 cid:95 ecl:hzl

byr:2000
hgt:165cm
iyr:2017 pid:519443292 eyr:2029 cid:240 hcl:#a97842
ecl:blu

cid:67 pid:038299774
eyr:2023 iyr:2015 hgt:179cm byr:1941 hcl:#18171d ecl:amb

byr:2000
eyr:2025 ecl:oth iyr:2017
pid:334154607
hcl:#fffffd hgt:173cm

hcl:#888785 ecl:amb
cid:131 iyr:2018 byr:1996 eyr:2026
hgt:180cm pid:709543988

iyr:1988
pid:263277424
hcl:ee8912 byr:1942 ecl:gry eyr:2040 hgt:161cm

eyr:2020 byr:1966 iyr:2020 hgt:169cm pid:611918000
hcl:#7d3b0c ecl:hzl

hgt:164cm ecl:brn
iyr:2015 pid:192054454 hcl:#6b5442 byr:1987 eyr:2022

byr:1952
ecl:zzz
pid:215953654
eyr:2021 hcl:#efcc98 hgt:153cm iyr:2026

hgt:167cm
hcl:#b6652a pid:847614726
eyr:2022 ecl:gry byr:1990 iyr:2015

hgt:185cm ecl:oth iyr:2012
byr:1933
cid:250
pid:038674023
hcl:#c0946f

pid:613273980 hcl:#a97842
ecl:oth byr:1924 hgt:179cm
eyr:2027 iyr:1950

hcl:#cfa07d byr:2018 hgt:190cm pid:64530329
ecl:brn
iyr:2024

hcl:z hgt:70cm pid:18807747
cid:284 byr:2023
eyr:2035 ecl:#4a1501
iyr:1954

iyr:2016 hgt:152cm pid:886247173 byr:1940 hcl:#c0946f eyr:2027 ecl:oth cid:150

hgt:152cm hcl:#48cfdf eyr:2025 cid:277
ecl:oth pid:246230621 byr:1932
iyr:2020

ecl:amb pid:871180042
cid:117 hcl:#602927 iyr:2011 hgt:152cm
eyr:2030 byr:1999

eyr:2024 ecl:hzl hgt:171cm
byr:1934 pid:356408125 iyr:2019 hcl:#b6652a
cid:169

eyr:2023
hcl:#7d3b0c
byr:1934 hgt:67in ecl:oth pid:191785527
cid:117 iyr:2016

iyr:2029
hcl:#602927 eyr:2022 byr:1931 ecl:oth hgt:192cm
pid:231475143

ecl:grn iyr:2014 cid:250 hcl:#b6652a byr:1970 pid:675238417 hgt:162cm
eyr:2026

ecl:brn
hcl:#623a2f eyr:2021 pid:293293433 hgt:158 byr:1977 iyr:2019

ecl:oth hcl:#ceb3a1 pid:013111996 eyr:2023 hgt:180cm byr:1976 cid:224

hgt:61cm
eyr:2027 ecl:amb pid:181cm iyr:1932
byr:1974
hcl:#18171d

byr:1968 hgt:167cm
hcl:#a97842 eyr:2022 iyr:2018 ecl:hzl pid:940968694

iyr:1943
hgt:96
cid:229
hcl:z eyr:1990 byr:2007 pid:#25aa73
ecl:#74592e

hgt:182cm iyr:2018 ecl:hzl eyr:2029 byr:1946 pid:602345030
hcl:#ceb3a1

pid:750306036 eyr:2020 hgt:181in ecl:xry
iyr:2011 hcl:z byr:1971 cid:71

pid:183825747 iyr:2019 hcl:#6b5442
byr:1974
hgt:180cm eyr:2028
ecl:amb

ecl:brn cid:200 pid:576495225
byr:1924
hcl:#efcc98 eyr:2022 iyr:2017 hgt:185cm

iyr:2020 hgt:167cm byr:1965 ecl:brn hcl:#888785
eyr:2028 pid:752062953

byr:2026
hcl:z
eyr:2020
ecl:#b4ec74 pid:187cm iyr:1974
cid:326 hgt:150cm

byr:1996 pid:507323629
iyr:2015 cid:347 eyr:2026 hcl:#efcc98
ecl:amb hgt:157cm

byr:2017 pid:456780590 hcl:#888785 eyr:1966 ecl:amb iyr:2023 cid:187 hgt:62cm

ecl:hzl iyr:2015 hcl:#6b5442 hgt:152cm eyr:2028 byr:1982 pid:003269467

iyr:2017 eyr:2026
ecl:blu cid:70 hcl:#7d3b0c
byr:1966 pid:160330947 hgt:189cm

iyr:2010 ecl:amb
hgt:164cm eyr:2029 byr:1963
pid:596606374 hcl:#efcc98

hcl:#fffffd cid:277 pid:102326370 hgt:154cm eyr:2026 iyr:2012 byr:1968
ecl:hzl

ecl:oth pid:477189554 hcl:#6b5442 eyr:2022 byr:1948 hgt:74in cid:181
iyr:2016

hgt:169cm hcl:#d7bc93
cid:344 ecl:oth
pid:#09c55d iyr:2017
eyr:2030 byr:1928

hcl:5d02ff ecl:#ca7901 iyr:1959 byr:2006 eyr:2022
hgt:164in
pid:#d6cdfd

ecl:amb pid:5739190196 eyr:2021 hgt:157in hcl:#efcc98 byr:2018 iyr:2028

byr:1995 ecl:hzl
iyr:2017
hcl:#a97842 pid:917039291 eyr:2026 hgt:175cm

iyr:2017 pid:756519868
hcl:#623a2f
eyr:2028
hgt:158cm
ecl:amb byr:1957

iyr:2012
hgt:158cm
byr:2014 pid:973021666 hcl:f04766 eyr:2035 ecl:utc

ecl:blu
byr:1989 eyr:2022
pid:520765501
cid:200 hgt:193cm hcl:#a97842 iyr:2011

byr:1959
ecl:blu hcl:#733820 cid:284 hgt:162cm
eyr:2022 pid:751629408 iyr:2016

byr:1978 cid:301
ecl:oth hgt:67cm hcl:#888785
eyr:2040 iyr:2025 pid:26038514

iyr:2020 byr:1974 hgt:163cm ecl:blu hcl:#7d3b0c eyr:2028 cid:99

hcl:#a97842
hgt:186cm
ecl:grn byr:1969 pid:460360492 iyr:2011 eyr:2028

byr:2009
pid:489490924 eyr:2031
hcl:cb5351 ecl:#083a25 hgt:164cm

iyr:2019
hcl:3463cc ecl:amb pid:4089063078 eyr:2022 hgt:150cm
byr:2007

eyr:2028 hcl:#ceb3a1
hgt:191cm iyr:2019 pid:737842199 ecl:blu cid:268 byr:1925

pid:868397851
hcl:#efcc98 ecl:grn iyr:2017 eyr:2021 byr:1943
hgt:179cm

hcl:#623a2f byr:1987 eyr:2023 iyr:2019 hgt:152cm
pid:473569020
ecl:grn

pid:953968630
hgt:175cm
byr:1971 ecl:blu hcl:#623a2f iyr:2017 cid:336 eyr:2030

ecl:grt hgt:74cm byr:2022 eyr:2024 pid:39114027
iyr:2026 hcl:4b5675

pid:#492988
eyr:2032 hgt:63cm iyr:2006
ecl:#817211 byr:2019

pid:800367032 hcl:#341e13
ecl:#765111 iyr:2012 byr:2006 hgt:166cm cid:291 eyr:2027

eyr:2021 iyr:2012 pid:876581393 ecl:amb hcl:#866857
hgt:64in byr:1993

iyr:2017 byr:1996 ecl:hzl pid:038990744
eyr:2028
hgt:177cm
hcl:#c0946f

hcl:#4214a6
eyr:2021
iyr:2019 cid:72 byr:1939
ecl:hzl pid:783071912 hgt:187cm

eyr:2020 hgt:158cm
pid:274060737 cid:277
iyr:2015 hcl:#bf9b5e byr:1950 ecl:brn

byr:1921 hcl:#7d3b0c cid:329 hgt:155cm eyr:2030 pid:718399669 iyr:2011 ecl:brn

cid:147 eyr:2021 hgt:167cm iyr:2010 ecl:grn byr:1975 hcl:#6b5442
pid:285479783

hgt:187cm
byr:2004 eyr:2025 hcl:bb331b
pid:851189955 iyr:2016
ecl:amb

hcl:#94007d pid:361561551 byr:1927 eyr:2026 iyr:2020
ecl:gry hgt:158cm

byr:1993 pid:#24c4af iyr:2023 hgt:175cm eyr:2028
hcl:z ecl:hzl cid:308

byr:1985 hcl:#c0946f eyr:2034 hgt:172cm
cid:300 iyr:2013 ecl:gry pid:389455676

eyr:2030 iyr:2017 byr:1956 hgt:178cm
pid:864401853 hcl:#6b5442

pid:836559549
iyr:2011
hgt:167cm
ecl:amb hcl:#c0946f
eyr:2026 byr:1981

pid:111085991 iyr:2011
ecl:blu eyr:2026 cid:311
byr:1920 hgt:182cm hcl:#602927

ecl:oth pid:284436132
byr:1929 cid:121
eyr:2027
iyr:2010
hgt:75in
hcl:#6b5442

byr:1987
hcl:#7d3b0c iyr:2018 hgt:180cm
ecl:blu eyr:2029 pid:878348021

hgt:183cm cid:98
byr:1953 hcl:#866857 eyr:2021 iyr:2012 pid:158898193

eyr:2030 pid:039638764 ecl:hzl hgt:190cm byr:1926
cid:294 hcl:#b6652a iyr:2017
"""
INPUT_STRING_5 = """
FFBFBFBRRL
FBFFBFBLRR
FFFBBFBRLR
FBBFFBFRRR
FBBBFFFLRR
FBBBFFBRRL
FBBBBFBRRL
BFBBFFBLLL
BBFFFFFRRR
BFBFFBFLRR
FBFFFBBRRR
BFBFBFBLRR
FFFBFBBRRL
BFBFFBFRRL
FBFFFBBRLR
FFBBFFBLRR
FFBFBBBLLR
FBFFBFBLLR
BBBFFFFLRR
FFBBBBBRLR
FBBBBFBLLL
FFFBFBFLRR
FFBFFFFRLL
FBBFFFFRRR
BFFFBBFRLR
BFBBFFFLRR
FBBBBFBRRR
FBFFBFBLLL
BBFBFFFRRL
FBBBFBBRRR
BBFFFFBLLL
FFFBFFBLRR
FFBFFBBRLL
BBBFFFFRLL
BFBBBBBLRR
FFBBFBBLRL
BFBFBFFLLL
FBFBBFFRLL
FFFBBFBLLR
FBBBBBFRRL
BFBFBBBRLR
FBBBFBFLLL
FBBFFFFLRL
BFBBBFBRRL
FFBBFFFRRR
BFBFBFFRLL
FBFBBBBLLR
FBFBBBFRLL
BFFBBBFLRR
BFFFBBFLLR
BFBFBBBLRR
BFBFFFBRRR
BBBFFFFLRL
FBFBBFFLRL
FBBFFBBLLR
FBBFBFBRLL
FBFFBBFRLR
BFBFBBBLLL
FBBFBBFLLL
BFBFBBBRLL
BBFFFFFRLL
BFBBFFFLLL
BFFFFFFRLR
FBFFBFFLRR
FFFBBBFRLR
BFFBBBFRRL
BFBBFBBRRL
BFFBBBBRLR
BBFBFFFRRR
FFFBFFBRLR
BFBFBBFLRL
BBFFFFBLRL
BBFFBBFRLL
FBBBFBFLRR
BFFBBBFLLL
BFBFBFBRRR
FBFFFBFRRL
FBBBFFFRLL
BFFBBFFRRL
BFFFBFBLLR
FBBFBFFLLR
BFBFBFBLLL
BBBFFFFRLR
FFBFFFFLRR
BFBFBBFRRR
FBBFBFFRLR
BFFFFBFLLL
FFBFFFFRRL
FBFBBFBRRL
FBFBBFBLRR
BFBFBFBRLL
FFBFBFFRRR
BFFFBFFRRR
FBFBFFFRRL
FFFBBFFLRR
FBBFFBFRRL
BFFFBFFRLR
BBFBBBBRLL
BFBFBBBLLR
BFFFBBFLRR
FFFBFFFLRL
BBFBFFFLLR
FFBBBFFRRR
FBBFBBFLRR
FBBFFFFLRR
FBBFBFBRRL
FFFBBBBLRL
BBFFFFBRLL
FBFBFFBRLL
BFFFFFFLLL
BFBBBBFRLL
FBBBFFBRRR
BFFFBBBRLR
FBBBBBBRRL
FBFFBFBRLL
FBBFBFBLLR
BBFFFFBRRL
BBFBBBFLLR
FBFBBFFRLR
BBFBBBFRLR
FFBFFFBLLL
FBFFFBBLRR
BBFFBFFRLL
FBFBFFFRLL
BFFFFFBRLR
FBFBBBBRLL
BBFBFFBLLL
FFBFFBFRLL
FBBBBBFRRR
BFBFBBFRLR
FFBFFBBLRR
FBFFFBBRLL
FBBFBFBLRL
FBBFBBBLLR
BBFFBBBLRL
FFFBFFBRLL
BFBBBFFRLL
BFFBFFFLRL
BFFFFFBLLR
FFBFBBBRRR
FFBFFBBLRL
BBFBBBFRLL
BFFBBBFRRR
BFBBFBFLLR
FFBFFFFRRR
FBBBFFFLLR
FFFBFBBLRR
FBBBBFBRLR
FFFFBBBRLL
BFBBFBBRLL
FFFBBBBRLR
FBFFFFFRRR
FBBBBBBRLR
FFBFBFFRLL
BBFBFFFLLL
BBFFFBFLLL
BFBFBFFRLR
BFFBBFBLLL
BFFFFFBLRR
FFBBFFBRRR
FFFBFBBRLL
FFBFBBBLRL
BFFBFFBLRL
BBFBFBBRRL
BFFBFFBRRL
BFFBBFBRLR
FBBBBBFLLL
BBFBBFBRRR
FFBBFFFRLR
FFFBFFFRLR
BFBBBFBLLR
BBFBFBFRLL
BBFBFFBRRR
FBBBBFBRLL
BFFFFBBLRR
FBFBFFFRRR
BFBFBFBLLR
BFBBFFBLRR
FFBFBFBLRR
FFBFBFBLLR
FFBBBFFLRR
FBFBBBBRRR
FBFFBBBLRL
BBFBBFFLLL
BFFFBFFLRL
BFBFFBFRRR
BFFBFBBRRR
FBBBBBFLRR
BFBFFFFLRR
FFBBFFFRRL
FBBFFFFLLL
FBBBFBBLLR
BBFFFBFRRR
BFBFFFFRLL
BBFFFFBLLR
FBBBBBFRLR
FBFFBBBRRR
BFBBBBBLLR
BFFFBBBLRL
BFFBFFBLLR
BFFBFFFLLL
FFBFFFBRLR
FBBFFBFRLL
FBFFBBFRRL
FFFBBFBLLL
FFFBFFFRLL
BFFFFBFLLR
FBFFFFFRLL
FFBBBBBLLL
FBFFFBBLRL
FBBFFBBRLL
BFBBBBFRRR
BFBBBBFLLR
BBFBBBFLLL
BFFBFBBRLR
FBBBBBBLRR
BFBFFFFLLR
BFBFBFFLRR
FBBFBFBLRR
BFBFBBBRRL
BBBFFFBLLL
FFBBBFBRRL
FFBBBFBRLR
BFBBBFBRLR
BFBBFFBLRL
FBFFBFFLRL
BFBBFBBRLR
FFBFFBFLRL
BFFBBBFRLL
FBFBFBFLLL
BFBBBFFLRR
FBFBBBBRRL
BFFBFBBRLL
BBFBBFFLRR
FBFFBFFLLL
FFBBBFBLLR
BBFFFFFLLL
FBFBFBBRLL
FFBFFBFRLR
BFBBFBFRLL
FFFBFFFLLL
FBBBFBFLLR
FBFFFBBLLL
BFFFBFFRLL
FBBFFFFRRL
FFFBFBFRRR
FBFFFFFLLL
BFBFFBFLLL
BFFBBFBRRL
BFFBBBBRLL
FBFFFFFLLR
BBFBBFBRLR
BBFBFBBRLL
BBBFFFFRRL
FFFBBFBRRR
FBBBBFBLRL
FFBBBFFRLL
BFBBFBFRRL
FBBBBFFRRR
FBFBBBBLRL
BBFBFBFRRL
BBFFBFBLLR
FFFFBBBRLR
FFBBFBFRRR
BBFBFBFLLL
BBFFFBBLLL
FBBBBFFLRL
BBFFBBFLRR
BFFFFFFRLL
BBFFBFBLRL
FFBBBBFRLL
BFBFFBBRLL
FBBBFFBLLL
BFFBFFBLLL
FFFFBBBRRR
FFFBBFFLLR
BFBFFFBLRL
FBFBBBFLRR
FBBFBFBRRR
BFFFFFBRRR
BBFFBBFRRR
BFFFFBFRLL
FFBFBBFLLL
FBFFBBFLLR
BFFBBFBRRR
BBFFBFFRLR
FBBBBBBLLR
BFBFBFBRLR
BBFBBFBLRR
FFFBFBBLLL
FBFBFFFRLR
BFBFFBBRRL
FFBBFBBLRR
BBFBFFBLLR
BFFBFBBLRL
FBFFBFBRRL
FFBBFFBLLL
BFBFFFFRLR
FBFFFBFRLL
FBBBFBBRLL
FFFBBBFLLL
FBBFBBBLRR
FFBFFBBRRL
FFFBFBBRLR
FBFFBBBRRL
BBFBFBFRRR
BFFBFBFLLR
FBFFFBFRLR
BBFBBBBLRL
FFFBBFFRRL
FBFBFBFLLR
FFBBBBFRRR
BFFFBFBLRL
BFBBBFBLRR
BFFBBFBLRL
FFBBFBFRRL
FFBBBBFLLR
BFFBFFBLRR
FBBFFBBLLL
FBBBBBFRLL
FBFBFBBLLL
FBBBBFFRLR
BBFFFFBLRR
BFFBBBBLRL
BFFBFBFRLR
FFBBBBFRLR
FBBBFFFLLL
BBBFFFFRRR
BBFBFBFLLR
FBBFBBBLLL
BBFFBFFRRL
BFFFBFBRLL
FFFBFBFLLL
FBBBBBFLLR
FFBBBBFRRL
BFFFBBFRLL
FFBFFFBLLR
FFBFBFBRLR
FFBFFBFLRR
FBBFBFFRRL
FBFFFBFLRL
BFBBBFFLRL
BFFFBBFRRR
BBFFFFBRLR
FBFFBBBLRR
BBFFBBBRRL
FBFBFBBRRR
FFBBBFBRRR
BBFFFFFLLR
FBBFBBFRLL
BFFFFFFRRR
BBFBFFFRLL
FBFBBFFRRL
FFFBFFBLLR
BFBBFFFLLR
FBBFFBBRLR
BFFBFBFLRL
FFFBBFFLRL
BFBFFFFRRR
BFFBFFFRRR
FBBFBFFRLL
BBFFBBFRLR
BFBBBBBLRL
FFBBFFFLRL
BFFBFFBRRR
FBBBFFBLLR
BBFBFFFLRL
FBFFBBFLLL
FFFBBFFRRR
FFFBFBFRLR
FFBBFBFRLR
BFBFFFFLLL
FBFBBFFLRR
BFFFBBFRRL
FBBFBBFRLR
FFFBFBFRLL
BFFFBFBRLR
BBFFFBFRLL
FBBBFBBRRL
BBFBBFFRRR
FFFBFFFRRL
BBFBBFFLLR
BBFFBBFRRL
FFBBFFBLLR
BBFFBFBRLL
FBBBFBBLRR
BFFBFFBRLR
BFFBBBBLLR
FFFBBFFLLL
BFFFBFFLLL
BBFFBFBRLR
FBFBFBFLRL
FBBBBFFRRL
BBFFFBBLRR
FFFBFBBRRR
BFBBFBFRLR
BFBBFBFLLL
FFFBFBBLLR
BFBBFFFRLL
FBBFFFFRLL
BFFFBFBLRR
FFBFFBBRRR
FFFBBFFRLL
BFFFFBFRRL
BBFBBFBRRL
BFBFFBBRRR
FBFFBFFRLR
BFFBFBFRLL
BFBFBBBLRL
FFFBBFFRLR
BFFFFFBLLL
FFFBFFFLRR
FBBFFBFLRR
FBFBBFFLLL
BFFBFBBLRR
BFFFFFFLRL
FFFBFFBLRL
BFFBBBBLLL
BFFFFFBRLL
BBFFBFFLRR
BFFBBFBLRR
BFFFBFFLLR
BBFFBFBLRR
BFBBBBBRRL
FBFBFFFLRR
FBFBBFFRRR
FBFFBBFLRL
FBFFFFBRRL
FFBBBBBLRR
BFFFFBFLRR
BBFBBBFRRR
FFBBBFBRLL
FBBFFFFLLR
BFBBBBFLRR
FFBFFFBRRL
BFBBFBBLRL
FFBBFBBRRR
FBBBFBFRLL
FBFBBBFLLL
BFFFFBBLRL
BBFBFBBLRR
FFFBFBFRRL
FBBFFFBRLL
BFFFFFFRRL
FBFFFBFLLL
BFBBBBBRLR
BBFBBBFLRR
FBBBFFBLRR
BBFFBBBLRR
FFFBFBFLLR
FBBBFBFRRL
BFFFBBFLRL
FFFBBBBLRR
BFBBBBFRLR
BBFBFBBLLR
BFBFBBFLLR
FBBBBBBLRL
BFBFFBBLLL
BFFFBFFRRL
BFFBBFFRRR
BBFFFBBRLL
FBBBBFFLLL
BFFFFFFLRR
BBFBBBFRRL
BFBBFBFRRR
BFBFBFBRRL
BFBFFFBLRR
FBBFBBBRLR
FBFBBFBRLL
FBFBFFBRRR
BFBBFBFLRR
BFBBFBBRRR
BFBBFFFLRL
FBFFFFFRLR
BBFFBBBLLL
BFBBFFBRLL
FBBBFFFRLR
FFBBFBBRLL
FBFBBBBRLR
BBFFBFFLLL
BBFFBBBRLL
FBFFFFBRLL
FFBBFBBLLL
FFBFFFFLRL
BBFBBFBLLR
FBFBFBBLRR
FFBBFFFLLL
BBFBFBBLLL
BFBFFFFRRL
FFBFBFFLRL
BFFBFFFRRL
FBFFFFFRRL
BBFBFBFRLR
FFBBBFBLRL
BFBBFFBRRR
BFBBBBBRRR
BBFFBFFLLR
FBBFFBBRRL
BFBFFFBRLR
FFFBBBFRLL
FFFBBBBRLL
FFBBBBBRRR
BBFBBBBLRR
FBFBBBBLRR
FBBFFBFRLR
BFFFFBFLRL
BFBBFBBLLL
FBBFBBBRLL
FFBBFBFLRR
BFBFBBBRRR
FFBFBFFRRL
BFFFFBFRRR
FBFBBFFLLR
BBFBBFFLRL
FBFFBBBRLL
FFBBFBBRRL
FFBFBFBLRL
BBFFBFBRRL
FFFBBBFLLR
FBFFBFFRRL
FFBFBFFLRR
BFFBBFFRLR
FFBFBFFRLR
BBFBFBBRRR
FBFBBBFLRL
FBFFBBFRRR
BFBFBFFLRL
FBBBFFBRLL
BFBFFBFRLR
BBFBFBBRLR
FBFBFFFLLL
FBFFFBBLLR
FBFFBFFRRR
FFFBBFBLRR
FFBFBFFLLL
BFFBBFBRLL
BFBFFFBLLR
BFFBBBFLLR
FBBFBFBRLR
FBBBFBFLRL
FBFFBBBRLR
FFBBBFFLRL
FFFBBBFLRL
BFFBBBFLRL
FFBBFFFLRR
FFBBBBFLLL
BFFBFFFRLR
FFBBBFBLRR
FFBBBFFRLR
BFFBBFFLRL
FBBBFFFLRL
BFFFBBBLRR
FFFFBBBLRR
BBFFFFBRRR
FBBFFFBLLR
BFBFFBFLRL
BFBBFFBRLR
BFBBBBFRRL
BFBFFBBLRL
FBBBBFFRLL
BFFFFBBLLL
FBBBFFFRRL
FFBBFBBLLR
BFBBBFFLLR
FBFBFBBLLR
FFBFFBFRRL
BBFBBFFRRL
BFBBBBBLLL
FBFBBFBLLL
BBFBFFBLRR
FBBFFBFLRL
BFFBFBBLLR
FFBFBBFLRR
BBFFBBBRLR
FFFBBBFRRL
BFFBBBFRLR
FBBBFBBLLL
FFBFFFFLLR
FBBFFFBRRL
BBFFBBFLLR
BFBBFBBLRR
FFFBFFBRRL
FFBFBBBRLR
FBBFFFBRLR
BFBFBFFRRR
BBFFFBBRLR
FBBBBFBLLR
BFBBBBBRLL
FBFBFBBRRL
FBBFFBBRRR
BBFFFBFLRL
FBBBBFFLRR
FBBFBFFLLL
FBBBFFBLRL
BFBBBFFRLR
BFBBFFBRRL
FFBFBBBLRR
BFFBFBFLLL
BFFFFBBRLR
BFFBFBFRRR
BFFFBBBRRL
FBFBBBFRLR
FBBBFBBRLR
FBFFFFFLRR
BFFFFBFRLR
BFBFFBFRLL
BBFBBFFRLL
FBBBFBFRLR
BBFBBBBRRL
BFBBBFBRLL
BBFFFFFLRR
FBFFFFBRLR
BFBFBFFRRL
FBFFBBBLLR
BBFFFBBRRR
BFBFBFFLLR
BBFFBBFLRL
BFBBFFBLLR
FFFBBFBRRL
BFFBBBBRRL
BFBBBBFLLL
BFFFBBBLLL
BBFBBFBLLL
BBFBBFBRLL
FFBFFFFRLR
FFBFBBFLRL
BFFBBBBRRR
FBFFBFBRRR
BFFFBFBRRL
FFBFFFBLRR
BFBBBFBLRL
BBFBBFFRLR
FBFBFBBLRL
FBBFFBBLRL
BFFFFFBLRL
BFFFBBBLLR
FBBFBBBRRR
BFBFFFFLRL
BFBBBBFLRL
BFBBBFBLLL
FBFBBBFRRR
FBFBFFBRRL
BFFFFFFLLR
FBBBBBBRLL
FFBBFBFLRL
FFBFFBFLLR
FFBFFFFLLL
FFBFFBFLLL
BFBFBBFLRR
FBFFFBBRRL
FBFFFBFRRR
FBBBFBFRRR
FFBBFFFLLR
FBBFBBFLRL
BFBBBFFRRR
FBFBFFBLRR
BBFBBBBLLR
BBFFBBBRRR
BBFFFBFLLR
BFBBFFFRLR
FBFFFBFLLR
FFBFBBBRRL
FFFBBBFRRR
BFBBFFFRRL
FBBFBBFRRR
FFBFBBFRRL
FFFFBBBRRL
BBFFFBBLRL
BFBFBBFRRL
FBBBBBFLRL
FBBBBFFLLR
FBFFFBFLRR
FBFFBFBLRL
FFBFBFBRLL
BFBBFFFRRR
BFFFBFBRRR
FFBFFFBRLL
FBBBFBBLRL
BFFFFFBRRL
BFFBBFBLLR
BFFBBBBLRR
BFFBFFFLLR
FBFFBFBRLR
BFFBFBBLLL
FBFFBBBLLL
BBFBBBBRLR
BBFFFBFLRR
FBFBBFBRRR
BBFBFFBLRL
FFFBFBBLRL
FFFBBBFLRR
BFBFFBBLRR
BFBFBBFRLL
FBBFBFFRRR
FFBFFBBLLR
FFBFFFBRRR
FBFBFBBRLR
BFBBFBBLLR
FBFFBBFLRR
BBFFFBFRLR
FFBFBBFRRR
BBFFFBBLLR
BBFFFBFRRL
FFFBBBBLLR
FBBFFFBLLL
FFBFFFBLRL
BBBFFFFLLL
FFBBBFFRRL
FBFBFFFLRL
FBBBBBBLLL
FFBFBBFLLR
BFFFFBBRRR
FBBFFBBLRR
BBFBFFBRRL
FFFBBFBLRL
BBFFBBBLLR
FFFBFFFRRR
FFFBBFBRLL
BFFBBFFLRR
BBFBBBBLLL
BFBFFFBRRL
BBFFBFFRRR
FBBFFFBLRR
FBBBBBBRRR
FFFBFFBRRR
FBFBFBFRRR
BBFFBBFLLL
BBFBFBBLRL
FFBBFBFRLL
BBFBFBFLRL
BFBFBFBLRL
FBFFFFBRRR
FFFBBBBLLL
FFBBFFBRLR
BBFFFFFLRL
BFFBFBBRRL
FBBFFBFLLL
BBFFBFBRRR
FFBBBBFLRL
FFBBFBFLLL
BFFFBBFLLL
FFBBBBFLRR
FBFFBBFRLL
BBFBBBBRRR
FBFBFFFLLR
FBFFFFFLRL
BFBFBBFLLL
BFBFFBBLLR
FFBBBBBLRL
FFBFBBFRLR
FBFFFFBLLR
FBFFBFFRLL
FBBFBBFRRL
FFBFFBFRRR
FBBBBFBLRR
FBBFBFFLRL
FBBFBBFLLR
FBFBBFBRLR
BBFFBFBLLL
BBFBFFFLRR
FBFBFBFLRR
BBFBFFBRLL
BBFBFFBRLR
BFBBBFFLLL
BFFBFBFRRL
BFFFFBBRLL
BFFBBFFLLR
BFFBFBFLRR
BBFBFBFLRR
BFFFBFBLLL
FFFBFBFLRL
FFBFBBBLLL
BBFBBFBLRL
FFBBFFBRLL
BBFBBBFLRL
FBBBFFBRLR
BFBFFFBRLL
FFBFBBBRLL
BFBFFBFLLR
FFBBBBBRLL
FFBFBFBRRR
FBFBFFBLRL
FFBBFFFRLL
FFBBFFBLRL
BFFBBFFLLL
BFFFBBBRLL
FFBFFBBRLR
BFFFBFFLRR
BFFFBBBRRR
FFBFFBBLLL
FBBFBFFLRR
FBFBBBFRRL
FBFFFFBLRL
FBBFBBBRRL
BFFBBFFRLL
BBFFFBBRRL
FFBBFBFLLR
FFBFBBFRLL
FFBFBFFLLR
FFBBBFFLLL
FBBFBFBLLL
FBFBFFBRLR
FFBBFBBRLR
BFBFFFBLLL
FFBBBBBRRL
FFFBBBBRRR
FFBBBBBLLR
FBFBFBFRLL
FBFBFBFRRL
BBFFBFFLRL
FBFBBBBLLL
FBFBFFBLLL
FBBFFFBLRL
FFFBFFFLLR
BBFFFFFRLR
BFFFFBBLLR
FBFBBBFLLR
BFFBFFFRLL
BBBFFFFLLR
FBFBBFBLRL
FFBBFFBRRL
FBFBFBFRLR
BFBBBFBRRR
BFFFFBBRRL
FFFBBBBRRL
FFFBFFBLLL
FBFFFFBLRR
BBFBFFFRLR
FFBBBFFLLR
FBBFFFBRRR
BFBBFBFLRL
BBFFFFFRRL
FBFBBFBLLR
FBFBFFBLLR
FBBFBBBLRL
BFBBBFFRRL
FBBBFFFRRR
FFBBBFBLLL
FBFFBFFLLR
BFFBFFBRLL
FBFFFFBLLL
FFBFBFBLLL
FBBFFFFRLR
BFFBFFFLRR
FBBFFBFLLR
"""
TARGET_1 = 2020
