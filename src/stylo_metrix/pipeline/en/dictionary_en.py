# Copyright (C) 2022  NASK PIB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# https://semanticsimilarity.wordpress.com/function-word-lists/
# lemmas

FUNCTION_WORDS = """a about above across after afterwards again against all almost alone along already also although always am among
amongst amoungst an and another any anyhow anyone anything anyway anywhere be around as at be became because be before
beforehand behind be being below beside besides between beyond both but by can can could dare despite do do do do down during
each eg either else elsewhere enough etc even ever every everyone everything everywhere except few first for former
formerly from far furthermore have have have he hence she here hereabouts hereafter hereby herein hereinafter heretofore
hereunder hereupon herewith hers herself he himself his how however I ie if in indeed inside instead into be it its
itself last latter latterly least less lot lot many may I meanwhile might mine more moreover most mostly much must my
myself namely near need neither never nevertheless next no nobody none noone nor not nothing now nowhere of off often
oftentimes on once one only onto or other other otherwise ought our ours ourselves out outside over per perhaps rather
re same second several shall she should since so some somehow someone something sometime sometimes somewhat somewhere
still such than that the their their they themselves then thence there thereabouts thereafter thereby therefore therein
thereof thereon thereupon these they third this those though through throughout thru thus to together too top toward
towards under until up upon we use very via be we well be what whatever when whence whenever where whereafter whereas
whereby wherein whereupon wherever whether which while whither who whoever whole whom whose why whyever will with within
without would yes yet you your your yourself yourselves""".strip().split()

LW_AGREEMENT_ADDITION_SIMILARITY = """in the first place, not only, but also, as a matter of fact, in like manner, in addition, coupled with,
                                      in the same way, in the same manner, in the same fashion, in the same vein, first, second, third,
                                      in the light of, not to mention, in the same breath, to say nothing of, equally important, by the same token,
                                      again, and, also, besides, furthermore, moreover, then, equally, identically, uniquely, as well as, together with, of course, likewise,
                                      comparatively, correspondingly, similarly, additionally""".strip().split(", ")

LW_EXAMPLES_SUPPORT_EMPHRASIS = """in other words, to put it differently, for one thing, as an illustration, in this case, for this reason, to  put it another way,
                                    to put it simply, to put it bluntly, to put it succinctly, to put it in a nutshell, that is to say,that is to say, with attention to, by all means,
                                    notably, including, to be sure, namely, chiefly, truly, indeed, in fact, in truth, in reality, in point of fact, in point of truth,certainty,
                                    surely, important to realize, important to realise, another key point, first thing to remember, most compelling evidence,
                                    must be remembered, point aften overlooked, on the negative side, on the positive side,
                                    markedly, especially, specifically, expressively, surprisingly, 
                                    frequently, significantly, remarkably, unusually, uncommonly, for example, for instance, for one thing, for another thing, for that reason,
                                    in fact, in reality, in truth, in particular, to demmonstrate, to emphasize, to repeat, to calrify, to explain, to enumerate,
                                    such as, to point out""".strip().split(", ")

LW_EFFECT_RESULT_CONSEQUENCE = """as a resul, under those corcumstances, for this reason, henceforth, thus, because, then, hence, therefore, consequently, as a result, so, so that, thereupon, accordingly, as a consequence""".strip().split(", ")

LW_OPPOSITION_LIMITATION_CONTRADICTION = """although, in contrast, on the other hand, however, nevertheless, but, yet, still, nonetheless, despite, in spite of, on the contrary, rather than, at the same time, 
                                          even so, though, above all, in reality, after all, unlike, albeit, besides, as much as, even though, instead,
                                          whereas, conversely, otherwise, rather, notwithstanding""".strip().split(", ")

LW_CAUSE_PURPOSE = """in the event that, granted that, provided that, in case, in the event, as long as, for the purpose of, with the intention, with this in mind, in the hope that, to the end that, for fear that, in order to, seeing, being that, in view of, whenever, lest, in case, privided that, given that, only, even if, so that, so as to, owing to, due to, inasmuch as""".strip().split(", ")

LW_SPACE_LOCATION_PLACE = """in the middle, in the vicinity, in, to the left, to the right, in front of, on this side, in the distance, here and there,
                           in the foreground, in the bakground, in the middle, in the center of, adjacent to, near, nearby, next to, opposite, opposite to, 
                           here, there, where, from, over, above, below, down, up, under, between, further, beyond,
                           around, before, alongside, amid, among, beneath, beside, behhind, across, toward, towards, within, throughout, through, to the north, to the south, to the east, to the west, 
                           north, west, south, east, northwest, northeast, southwest, southeast, in the north, in the south, in the east, in the west""".strip().split(", ")

LW_TIME_CHRONOLOGY_SEQUENCE ="""time, all the time, at the persent time, at the moment, at the same time, at the same moment, at the same instant, sooner or later, 
                               in the meantime, in the interim, in the future, in the past, in the present, in the near future, in the near past, in the near present,
                               in the long run, in the long term, in the long haul, in the long distance, in the long time, in the long term, up to the present time, up to the present moment,
                               to begin with, in due time, in the end, until now, as soon as, as long as, in the meantime, in a moment, without delay,
                               in the first place, all of a sudden, at this instat, immediately, quickly, finally,
                               after, later, last, until, till, since, then, before, when, once, now, formerly, suddenly, shortly,
                               henceforth, whenever, eventually, meanwhile, further, during, in time, prior to, 
                               forthwith, straightaway, by the time, whenever, instantly, presently, occasionally""".strip().split(", ")

LW_MANNER = """how, as though, as if""".strip().split(", ")

LW_CONDITION = """if, only if, unless, until, provided that, assuming that, even if, in case""".strip().split(", ")