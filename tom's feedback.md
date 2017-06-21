
What's the thesis?

- R (ggplot2) has a consistent API for EDA; python doesn't
- Public service for "How do I do X in python?"

I think these two are compatible, so having them both in the post is fine (though if
someone is using it as a reference many times, the top-section is kind of a distraction).

I think a section at the end on why ggplot2 is "better" (maybe the quotes aren't needed) would
be good. Something about the consistency across examples?

Still, I would say that matplotlib+seaborn *are* consistent, but different than ggplot2. matplotlib
works with arrays of data. seaborn + pandas work with DataFrames and labels. So my rough rules are:

1. Use seaborn anytime you have faceting (including by color, which is a kind of faceting; see below)
2. Pass arrays to matplotlib, either directly, or by using one of Seaborn or pandas' abstractions

I recognize that I'm already familiar with this, so I probably underestimate the learning curve.
Still, I think it's fine.

Nit-picks

- Could use `sort=False` in `Basic Bar Chart`'s value_counts (can't remember if
preserves order, or is arbitrary thouugh)

"Scatter Plot with Colored Points by Category"

I would use seaborn

```
g = sns.FacetGrid(mpg, hue="class")
g.map(plt.scatter, "displ", "hwy").add_legend().set(
    title="Engine Displacement in Liters vs Highway MPG",
    xlabel="Engine Displacement in Liters",
    ylabel="Highway MPG"
)
```

"Stacked KDE Plot"

Again, seaborn

```
g = sns.FacetGrid(diamonds, hue="cut")
g.map(sns.kdeplot, shade=True).add_legend()
```