"""California hous prices examples"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_example.ipynb.

# %% auto 0
__all__ = ['get_bivar_rank']

# %% ../nbs/03_example.ipynb 8
# for core??
def get_bivar_rank(df,x,y,grid_size=3):
    x_ranks = [ascii_uppercase[x] for x in range(grid_size)]
    y_ranks = list(range(1,grid_size+1))
    bivar_ranks = [str(y)+x for y in y_ranks for x in x_ranks]
    
    x_rank_col=x[:3]+'_rank'
    y_rank_col=y[:3]+'_rank'
    
    df[x_rank_col] = pd.cut(df[x], grid_size, labels=x_ranks)
    df[y_rank_col] = pd.cut(df[y], grid_size, labels=y_ranks)

    df['BiVar_rank'] = df[y_rank_col].astype(str) + df[x_rank_col].astype(str)
    df['BiVar_rank'] = pd.Categorical(df.BiVar_rank, ordered=True, categories=bivar_ranks)
    
    return df

