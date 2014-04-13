This small script written in python is used to produce pdfs from standalone tikz
code. The file oranisation should be like this.

In the document:
	\begin{figure}
		\begin{tikzpicture}
		\input{picturecode.tex}
		\end{tikzpicture}
	\end{figure}

In the picturecode.tex:
	%This is direct tikz code.
	(3,-1) coordinate (a) node[right] {a}
	-- (0,0) coordinate (b) node[left] {b}
	-- (2,2) coordinate (c) node[above right] {c}
	pic["$\alpha$", draw=orange, <->, angle eccentricity=1.2, angle radius=1cm]
	{angle=a--b--c};